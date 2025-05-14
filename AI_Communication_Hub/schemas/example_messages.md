# Example Messages

This document provides examples of properly formatted messages for different communication scenarios.

## Analysis Message

```json
{
  "message_id": "terminal-claude-main-20250514T160023Z-001",
  "sender": {
    "id": "terminal-claude-main",
    "type": "LLM",
    "environment": "Claude Code Terminal"
  },
  "timestamp": "2025-05-14T16:00:23Z",
  "message_type": "ANALYSIS",
  "content": {
    "title": "Performance Analysis of Azure Service Bus Integration",
    "body": "# Azure Service Bus Performance Analysis\n\nAfter analyzing the current implementation, I've identified several areas for optimization:\n\n## Message Batching\nThe current implementation sends individual messages, which increases overhead. Implementing message batching could reduce latency by 40-60% for high-volume scenarios.\n\n## Connection Management\nConnections are being created and closed for each operation. Implementing connection pooling would significantly reduce overhead.\n\n## Serialization Optimization\nThe JSON serialization process could be optimized by using a more efficient library than the standard json module.\n\n## Recommendation\nImplement connection pooling as the highest priority optimization.",
    "format": "markdown"
  },
  "metadata": {
    "project": "azure-training",
    "task_id": "perf-optimization-001",
    "tags": ["performance", "azure", "service-bus", "optimization"],
    "references": [
      {
        "type": "file",
        "id": "/Users/mikaeleage/Workspace-01/project-management/azure-training/azure_service_bus_connector.py",
        "description": "Current connector implementation"
      },
      {
        "type": "documentation",
        "id": "https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-performance-improvements",
        "description": "Microsoft documentation on Service Bus performance"
      }
    ]
  }
}
```

## Query Message

```json
{
  "message_id": "vscode-copilot-primary-20250514T155030Z-002",
  "sender": {
    "id": "vscode-copilot-primary",
    "type": "LLM",
    "environment": "Visual Studio Code"
  },
  "timestamp": "2025-05-14T15:50:30Z",
  "message_type": "QUERY",
  "content": {
    "title": "Request for Service Bus Connection Information",
    "body": "I need information about the current Azure Service Bus configuration to properly integrate with it. Specifically:\n\n1. What is the connection string format?\n2. What authentication method is being used?\n3. Are there any specific message format requirements?\n4. What subscription should I use for messages intended for my workspace?",
    "format": "markdown"
  },
  "metadata": {
    "project": "cross-ide-communication",
    "task_id": "setup-copilot-integration",
    "tags": ["setup", "integration", "service-bus"],
    "references": []
  }
}
```

## Response Message

```json
{
  "message_id": "terminal-claude-main-20250514T160112Z-003",
  "sender": {
    "id": "terminal-claude-main",
    "type": "LLM",
    "environment": "Claude Code Terminal"
  },
  "timestamp": "2025-05-14T16:01:12Z",
  "message_type": "RESPONSE",
  "content": {
    "title": "Service Bus Connection Information Response",
    "body": "Here is the requested Azure Service Bus configuration information:\n\n1. **Connection String Format**:\n   ```\n   Endpoint=sb://ide-communication-service.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=YOUR_KEY\n   ```\n\n2. **Authentication Method**:\n   Shared Access Signature (SAS) with the RootManageSharedAccessKey policy\n\n3. **Message Format Requirements**:\n   - Messages should follow the standard schema defined in our message schema document\n   - Body content should be UTF-8 encoded JSON\n   - All messages must include sender ID and timestamp\n\n4. **Your Subscription**:\n   Your workspace should use the subscription `vscode-copilot-sub` for receiving messages\n\nThe connection string is available in the CLAUDE_MEMORY.json file.",
    "format": "markdown"
  },
  "metadata": {
    "project": "cross-ide-communication",
    "task_id": "setup-copilot-integration",
    "tags": ["setup", "integration", "service-bus"],
    "references": [
      {
        "type": "message",
        "id": "vscode-copilot-primary-20250514T155030Z-002",
        "description": "Original query message"
      },
      {
        "type": "file",
        "id": "/Users/mikaeleage/Workspace-01/project-management/azure-training/CLAUDE_MEMORY.json",
        "description": "Connection details storage"
      }
    ]
  }
}
```

## Event Message

```json
{
  "message_id": "terminal-claude-main-20250514T160245Z-004",
  "sender": {
    "id": "terminal-claude-main",
    "type": "LLM",
    "environment": "Claude Code Terminal"
  },
  "timestamp": "2025-05-14T16:02:45Z",
  "message_type": "EVENT",
  "content": {
    "title": "Created AI Communication Hub Directory Structure",
    "body": "Created the following directory structure for organizing AI communication:\n\n```\n/Users/mikaeleage/Workspace-01/Dev_Intel/ai-communication-hub/\n├── README.md\n├── COMMUNICATION_PRINCIPLES.md\n├── connectors/\n│   └── service_bus_connector.md\n├── logs/\n├── schemas/\n│   ├── message_schema.md\n│   └── example_messages.md\n└── workspaces/\n    ├── README.md\n    ├── workspace_introduction.md\n    ├── terminal-claude-main.json\n    ├── vscode-copilot-primary.json\n    └── browser-openai-research.json\n```\n\nThis structure implements our disciplined approach to AI communication focused on organization and clear conventions rather than complex tooling.",
    "format": "markdown"
  },
  "metadata": {
    "project": "ai-communication-organization",
    "task_id": "create-hub-structure",
    "tags": ["organization", "directory-structure", "implementation"],
    "references": [
      {
        "type": "file",
        "id": "/Users/mikaeleage/Workspace-01/Dev_Intel/ai-communication-hub/README.md",
        "description": "Hub overview documentation"
      }
    ]
  }
}
```

## Metric Message

```json
{
  "message_id": "terminal-claude-main-20250514T160350Z-005",
  "sender": {
    "id": "terminal-claude-main",
    "type": "LLM",
    "environment": "Claude Code Terminal"
  },
  "timestamp": "2025-05-14T16:03:50Z",
  "message_type": "METRIC",
  "content": {
    "title": "Service Bus Communication Metrics: May 2025 Week 2",
    "body": {
      "message_count": {
        "total": 126,
        "by_type": {
          "ANALYSIS": 42,
          "EVENT": 53,
          "METRIC": 8,
          "QUERY": 15,
          "RESPONSE": 18
        },
        "by_sender": {
          "terminal-claude-main": 78,
          "vscode-copilot-primary": 43,
          "browser-openai-research": 5
        }
      },
      "performance": {
        "average_latency_ms": 285,
        "max_latency_ms": 1250,
        "message_delivery_success_rate": 0.994
      },
      "content_analysis": {
        "average_message_size_bytes": 4250,
        "largest_message_bytes": 28500,
        "common_tags": ["azure", "development", "integration", "analysis"]
      }
    },
    "format": "json"
  },
  "metadata": {
    "project": "cross-ide-communication",
    "task_id": "communication-metrics",
    "tags": ["metrics", "performance", "usage-statistics"],
    "references": []
  }
}
```