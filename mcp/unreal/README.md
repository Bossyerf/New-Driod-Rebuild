# MCP: Unreal Control (UE 5.6)

Exposes actions to control Unreal Editor: open project, run PIE, issue console commands, run automation tests, create/edit Blueprints, manage plugins, and build/package.

Planned endpoints (FastAPI):
- POST /editor/console
- POST /editor/automation
- POST /blueprint/create
- POST /blueprint/edit
- POST /plugins/enable
- POST /project/open

Server will shell out to Epic's AutomationTool and/or Remote Execution. On Windows, run in sandboxed terminal when invoked via Cursor.
