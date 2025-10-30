from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import subprocess
import os

app = FastAPI(title="MCP Unreal Control", version="0.2.0")

class ConsoleCommand(BaseModel):
    command: str
    project_path: Optional[str] = None

class AutomationRequest(BaseModel):
    test_name: str
    project_path: Optional[str] = None

class BlueprintCreate(BaseModel):
    name: str
    path: str
    parent_class: str = "Actor"
    project_path: Optional[str] = None

UE_EDITOR_EXE = os.environ.get("UE_EDITOR_EXE", "")  # optional: full path to UEEditor.exe

@app.post("/editor/console")
def run_console(cmd: ConsoleCommand):
    # Placeholder: wire to AutomationTool/Remote Execution in next pass
    return {"ok": True, "ran": cmd.command, "project": cmd.project_path}

@app.post("/editor/automation")
def run_automation(req: AutomationRequest):
    # Placeholder response; hook to AutomationTool in follow-up
    return {"ok": True, "test": req.test_name, "project": req.project_path}

@app.post("/blueprint/create")
def create_blueprint(bp: BlueprintCreate):
    # Placeholder: will call an Editor Utility (Python) in next pass
    return {"ok": True, "blueprint": bp.name, "path": bp.path, "parent_class": bp.parent_class}
