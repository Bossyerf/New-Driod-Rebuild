from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI(title="MCP Vision", version="0.2.0")

class CaptureRequest(BaseModel):
    target: Optional[str] = None

@app.post("/capture/screenshot")
def capture_screenshot(req: CaptureRequest):
    # Stub: returns a static path where the UE automation would save a screenshot
    os.makedirs("captures", exist_ok=True)
    return {"ok": True, "path": "captures/last.png"}
