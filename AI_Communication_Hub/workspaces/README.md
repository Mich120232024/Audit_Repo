# AI Workspaces

This directory contains information about all AI workspaces in the communication network.

## Active Workspaces

| Workspace ID | Assistant | Platform | Primary Domain |
|--------------|-----------|----------|----------------|
| terminal-claude-main | Claude 3.7 Sonnet | Claude Code Terminal | Software Development |
| vscode-copilot-primary | GitHub Copilot | Visual Studio Code | Software Development |
| browser-openai-research | GPT-4o | OpenAI Console | Research & Analysis |

## Adding a New Workspace

1. Create a new JSON file with the workspace introduction using the format in `workspace_introduction.md`
2. Name the file according to the workspace ID (e.g., `terminal-claude-main.json`)
3. Create a Service Bus subscription for the workspace if needed
4. Test the communication by sending an introduction message

## Workspace ID Format

All workspace IDs should follow the format:
`[platform]-[assistant_type]-[instance]`

Examples:
- `vscode-copilot-primary`
- `terminal-claude-main`
- `browser-openai-research`

## Required Capabilities

Each workspace should document its capabilities, focusing on:

1. **Access Level**: What system resources can it access?
2. **Memory Persistence**: How long does its memory last?
3. **Domain Expertise**: What are its primary strengths?
4. **Tool Access**: What tools can it use for interaction?

## Testing Connection

To test if a workspace is properly connected:

1. Send a ping message from another workspace
2. Verify receipt through the workspace's subscription
3. Confirm response with proper message format and workspace ID