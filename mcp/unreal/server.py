from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MCP Unreal Control", version="0.1.0")

class ConsoleCommand(BaseModel):
    command: str
    project_path: str | None = None

@app.post("/editor/console")
def run_console(cmd: ConsoleCommand):
    # TODO: invoke UE editor console via AutomationTool/Remote Execution
    return {"ok": True, "ran": cmd.command}
