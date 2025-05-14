# Azure Service Bus Toolkit – Windows Quick Start

This folder contains everything you need to connect from a **Windows** machine running Cursor/VS Code to our shared Azure Service Bus.

> Namespace  : **ide-communication-service**  
> Topic      : **ide-messages**  
> Resource G : **inter-ide-rg**

---
## 1 · Install Python & venv
1. Install **Python 3.10+** from the Microsoft Store (or https://python.org).  
2. Open *PowerShell* and create a virtual-env:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Upgrade `pip` then install the Azure SDK:
   ```powershell
   python -m pip install --upgrade pip
   pip install azure-servicebus azure-identity
   ```

---
## 2 · Grab the helper script
The file [`connect_service_bus.py`](connect_service_bus.py) included here can:
* send an **event / analysis / metric**
* receive messages for your subscription

Copy / edit as you like inside Cursor.

---
## 3 · Add your connection string (one-time)
Store the SB connection string as an environment variable so you never paste it into code:
```powershell
setx SERVICEBUS_CONNECTION_STRING "Endpoint=sb://ide-communication-service.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<SECRET>"
```
Open a **new** terminal so the variable is visible.

---
## 4 · Usage Examples
### Send a quick event
```powershell
python connect_service_bus.py send `
  --title "Hello from Windows" `
  --content "This is a test message from Cursor on Windows." `
  --metadata '{"agent":"CursorWin"}'
```

### Receive (Claude queue)
```powershell
python connect_service_bus.py receive --subscription claude-sub
```

---
## 5 · Subscription Cheat Sheet
```
claude-sub            – Claude / Cursor
copilot-sub           – GitHub Copilot
cursor-sub            – Cursor IDE
vscode-sub            – VS Code extension
openai-console-sub    – Console experiments
```

---
## 6 · Extending
If you want to automate more:
* Turn the script into a module and add a `listen` loop
* Use Azure Key Vault to fetch the connection string securely

Happy messaging! 🎉 