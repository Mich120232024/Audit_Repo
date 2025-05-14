import os, json, argparse, uuid, datetime, sys
from typing import Dict, Any

from azure.servicebus import ServiceBusClient, ServiceBusMessage
from azure.identity import DefaultAzureCredential

# ---- helpers -------------------------------------------------------------

CONN_STR = os.getenv("SERVICEBUS_CONNECTION_STRING")
TOPIC    = "ide-messages"
SERVICEBUS_FQDN = "ide-communication-service.servicebus.windows.net" # As per README

if CONN_STR:
    print("[INFO] Using Service Bus Connection String from environment variable.")
    client = ServiceBusClient.from_connection_string(CONN_STR)
else:
    print("[INFO] SERVICEBUS_CONNECTION_STRING not found. Attempting to use DefaultAzureCredential.")
    try:
        credential = DefaultAzureCredential()
        client = ServiceBusClient(fully_qualified_namespace=SERVICEBUS_FQDN, credential=credential)
        print("[INFO] Successfully initialized ServiceBusClient with DefaultAzureCredential.")
    except Exception as e:
        print(f"[ERROR] Failed to initialize ServiceBusClient with DefaultAzureCredential: {e}")
        print("[INFO] Please ensure you are logged in with 'az login' and have appropriate permissions, or set the SERVICEBUS_CONNECTION_STRING environment variable.")
        sys.exit(1) # Exit if client can't be initialized

def build_message(msg_type: str, title: str, body: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": str(uuid.uuid4()),
        "messageType": msg_type,
        "title": title,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "sender": metadata.pop("sender", "CursorWin"),
        "metadata": metadata,
        "content": body,
    }

# ---- commands ------------------------------------------------------------

def cmd_send(args):
    meta = json.loads(args.metadata) if args.metadata else {}
    meta.setdefault("agent", "CursorWin")
    msg_obj = build_message(args.type.capitalize(), args.title, args.content, meta)

    with client:
        sender = client.get_topic_sender(topic_name=TOPIC)
        with sender:
            sender.send_messages(ServiceBusMessage(json.dumps(msg_obj)))
            print("✔ Message sent →", TOPIC)


def cmd_receive(args):
    sub = args.subscription
    with client:
        receiver = client.get_subscription_receiver(topic_name=TOPIC, subscription_name=sub, max_wait_time=args.wait)
        with receiver:
            msgs = receiver.receive_messages(max_message_count=args.max)
            if not msgs:
                print("No messages.")
                return
            for sbm in msgs:
                body = b"".join(part for part in sbm.body) if hasattr(sbm.body, "__iter__") else sbm.body
                if isinstance(body, bytes):
                    body = body.decode()
                try:
                    body = json.loads(body)
                except Exception:
                    pass
                print(json.dumps(body, indent=2))
                receiver.complete_message(sbm)

# ---- CLI -----------------------------------------------------------------

p = argparse.ArgumentParser(description="Simple Azure Service Bus helper")
subcmd = p.add_subparsers(dest="cmd", required=True)

s_send = subcmd.add_parser("send")
s_send.add_argument("--type", choices=["event", "analysis", "metric"], default="event")
s_send.add_argument("--title", required=True)
s_send.add_argument("--content", required=True)
s_send.add_argument("--metadata", help="JSON string with extra metadata")

s_recv = subcmd.add_parser("receive")
s_recv.add_argument("--subscription", required=True)
s_recv.add_argument("--max", type=int, default=10)
s_recv.add_argument("--wait", type=int, default=5)

args = p.parse_args()
{
    "send": cmd_send,
    "receive": cmd_receive,
}[args.cmd](args) 