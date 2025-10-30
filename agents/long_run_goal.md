Use this exact goal in Cursor (with Parallel + Cloud Agents enabled):

Goal:
"Autonomously master Unreal Engine 5.6 and rebuild the Andrio system end-to-end. Steps:
1) Verify MCP servers (unreal@http://127.0.0.1:8001, vision@http://127.0.0.1:8002) are reachable.
2) Ingest UE docs and E:\\UeSource; populate Chroma + Neo4j.
3) Build hybrid retrieval; validate with sample queries.
4) Implement real UE automation endpoints (console, tests, blueprint create/edit) in mcp/unreal/server.py.
5) Create a minimal UE test project; run PIE, console commands, and an automation test.
6) Add RL reward from test outcomes; store episodes.
7) Iterate: expand blueprint operations, plugin management, packaging; keep tests green.
8) Use the vision server to capture viewport screenshots and validate via qwen3:vl.
Continue iterating until basic mastery is achieved, then switch to interactive build tasks."

Notes:
- The stop hook is configured to auto-continue, enabling long sessions.
- Prefer Composer for iteration speed, compare with another model if needed.
- Keep the PC awake and use Cloud Agents for reliability.
