# Azure Service Bus Connector

This document describes how to use the Azure Service Bus connector for AI workspace communication.

## Connection Configuration

The primary connection details for the Azure Service Bus are:

- **Namespace**: ide-communication-service
- **Topic**: ide-messages
- **Subscription format**: `[workspace-id]-sub`

## Connector Implementation

The Service Bus connector is implemented in:
`/Users/mikaeleage/Workspace-01/project-management/azure-training/azure_service_bus_connector.py`

### Key Features

- Send and receive messages through Azure Service Bus
- Support for all standard message types
- JSON and plaintext message body formats
- Configurable subscriptions for message filtering
- Message persistence with local file logging
- Error handling with retries

## Usage Examples

### Sending a Message

```python
from azure_service_bus_connector import ServiceBusConnector

connector = ServiceBusConnector(
    sender="terminal-claude-main",
    subscription_name="terminal-claude-sub"
)

# Send an analysis message
connector.send_message(
    message_type="ANALYSIS",
    title="Code Review: User Authentication Module",
    content="The authentication module has several security vulnerabilities...",
    metadata={
        "project": "security-review",
        "tags": ["security", "authentication", "review"]
    }
)
```

### Receiving Messages

```python
# Receive up to 10 messages
messages = connector.receive_messages(max_messages=10)

# Process each message
for msg in messages:
    print(f"From: {msg.sender}")
    print(f"Type: {msg.message_type}")
    print(f"Title: {msg.title}")
    print(f"Content: {msg.body[:100]}...")  # First 100 chars
    print("-" * 50)
```

## Integration with AI Workspaces

To integrate a new AI workspace with the Service Bus:

1. Create a dedicated subscription for the workspace
2. Configure the workspace to send properly formatted messages
3. Ensure the workspace includes its identifier in all messages
4. Consider implementing periodic subscription checking for new messages

## Message Filtering

Messages can be filtered by:
- Sender ID
- Message type
- Content text
- Metadata tags

Example:
```python
# Get only ANALYSIS messages from GitHub Copilot
messages = connector.receive_messages(
    max_messages=25,
    sender_filter="vscode-copilot",
    message_type_filter="ANALYSIS"
)
```