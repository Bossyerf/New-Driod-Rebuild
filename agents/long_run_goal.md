Use this goal in Cursor with Parallel Agents (2) and Cloud Agents enabled.

Master goal:
"Autonomously master Unreal Engine 5.6 and rebuild the Andrio system end-to-end. Maintain safety, write tests, and keep iterating until green. When a step completes, immediately choose the next highest-impact task."

Agent split (run in parallel):
- Agent A — Ingestion + RAG/Graph
  1) Verify MCP endpoints are reachable (unreal@http://127.0.0.1:8001, vision@http://127.0.0.1:8002).
  2) Ingest UE docs and E:\\UeSource; populate Chroma + Neo4j.
  3) Implement hybrid retrieval (vector + graph) and write validation queries.
  4) Produce retrieval QA tests; iterate until retrieval quality is acceptable.

- Agent B — Unreal control + Tests
  1) Implement real UE 5.6 calls in mcp/unreal/server.py: console, automation test run, blueprint create/edit stubs wired to Editor/AutomationTool.
  2) Create a minimal UE test project; run PIE, console commands, and a basic automation test.
  3) Add RL reward from test outcomes; store episodes; keep tests green.
  4) Use the vision server to capture viewport screenshots and validate via qwen3:vl.

Coordination rules:
- Worktree isolation: each agent commits to its own worktree/branch. Prefer small, frequent PRs. Merge the better diffs.
- Models: run Composer (fast) on one agent and alternate model on the other (or higher temperature) to diversify approaches.
- If a dependency is missing, add it to requirements.txt and script setup. Keep Windows compatibility.
- Always add or update tests when introducing a new capability. Fix failing tests before proceeding.

Continue policy:
- Continue iterating automatically (stop hook). If auto-follow-ups are capped, resume by submitting once and continue.

Exit criteria for phase 1 (switch to interactive build):
- Ingestion fills Chroma + Neo4j with UE docs and E:\\UeSource coverage; retrieval QA passes.
- UE control endpoints execute successfully; a UE test project builds, runs PIE, and a sample automation test passes.
- Basic RL reward loop records episodes and improves pass rate over retries.
