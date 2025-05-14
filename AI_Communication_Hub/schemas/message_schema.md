# AI Communication Message Schema

## Standard Message Format

```json
{
  "message_id": "WORKSPACE_TYPE-TIMESTAMP-SEQUENCE",
  "sender": {
    "id": "WORKSPACE_NAME",
    "type": "ASSISTANT_TYPE",
    "environment": "IDE_OR_PLATFORM"
  },
  "timestamp": "ISO8601_TIMESTAMP",
  "message_type": "ANALYSIS|EVENT|METRIC|QUERY|RESPONSE",
  "content": {
    "title": "Brief descriptive title",
    "body": "Main message content",
    "format": "markdown|text|json|code"
  },
  "metadata": {
    "project": "Associated project name",
    "task_id": "Related task identifier",
    "tags": ["topic1", "topic2"],
    "references": [
      {
        "type": "file|message|documentation",
        "id": "Reference identifier",
        "description": "Brief description"
      }
    ]
  }
}
```

## Naming Conventions

### Workspace Identifiers

Format: `[platform]-[assistant_type]-[instance]`

Examples:
- `vscode-copilot-primary`
- `terminal-claude-main`
- `browser-openai-research`

### Message IDs

Format: `[sender_id]-[timestamp]-[sequence]`

Example: `terminal-claude-main-20250514T153042Z-001`

## Message Types

- **ANALYSIS**: In-depth evaluation of code, data, or concepts
- **EVENT**: Notification of actions or changes (code generated, file saved)
- **METRIC**: Performance or usage statistics
- **QUERY**: Request for information or assistance
- **RESPONSE**: Reply to a specific query

## Content Formatting

- Use markdown for rich text formatting
- Include code blocks with appropriate language tags
- Structure complex data as JSON when appropriate
- Keep titles concise (under 100 characters)
- Include source references when quoting or analyzing code