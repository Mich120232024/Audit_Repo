# AI Workspace Introduction Template

When a new AI workspace joins the communication network, it should introduce itself using this format to establish context and capabilities.

## Introduction Format

```json
{
  "introduction": {
    "workspace_id": "UNIQUE_WORKSPACE_ID",
    "assistant": {
      "name": "ASSISTANT_NAME",
      "type": "ASSISTANT_TYPE",
      "version": "VERSION_INFO",
      "provider": "COMPANY_OR_PROVIDER"
    },
    "environment": {
      "platform": "APPLICATION_OR_IDE",
      "location": "PATH_OR_CONTEXT",
      "user": "USER_IDENTIFIER"
    },
    "capabilities": [
      "CAPABILITY_1",
      "CAPABILITY_2"
    ],
    "domains": [
      "PRIMARY_DOMAIN",
      "SECONDARY_DOMAIN"
    ],
    "context_access": {
      "files": true|false,
      "project_structure": true|false,
      "execution": true|false,
      "web_access": true|false
    },
    "memory": {
      "persistence": "session|project|global",
      "limitations": "DESCRIPTION_OF_MEMORY_CONSTRAINTS"
    }
  }
}
```

## Example Introduction

```json
{
  "introduction": {
    "workspace_id": "terminal-claude-main",
    "assistant": {
      "name": "Claude",
      "type": "LLM",
      "version": "Claude 3.7 Sonnet",
      "provider": "Anthropic"
    },
    "environment": {
      "platform": "Claude Code Terminal",
      "location": "/Users/mikaeleage/Workspace-01",
      "user": "mikaeleage"
    },
    "capabilities": [
      "code generation and modification",
      "file system access",
      "command execution",
      "web search",
      "web fetch"
    ],
    "domains": [
      "software development",
      "system administration",
      "data analysis"
    ],
    "context_access": {
      "files": true,
      "project_structure": true,
      "execution": true,
      "web_access": true
    },
    "memory": {
      "persistence": "session",
      "limitations": "Session context limited to 200K tokens"
    }
  }
}
```

## Guidelines for Introductions

1. Be specific and accurate about capabilities and limitations
2. Include relevant domain expertise
3. Specify memory persistence level
4. Indicate access to project context
5. Use the standardized workspace_id format
6. Update introduction when capabilities or context changes