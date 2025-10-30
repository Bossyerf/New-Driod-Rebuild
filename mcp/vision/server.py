from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MCP Vision", version="0.1.0")

class CaptureRequest(BaseModel):
    target: str | None = None  # e.g., window title

@app.post("/capture/screenshot")
def capture_screenshot(req: CaptureRequest):
    # TODO: integrate with OS capture or UE automation screenshot
    # Return a placeholder path for now
    return {"ok": True, "path": "captures/last.png"}
