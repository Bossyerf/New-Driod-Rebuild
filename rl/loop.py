from typing import Dict, Any

# Simple reward shaping; integrate real UE signals later

def step(task: str, result: Dict[str, Any]) -> float:
    if result.get("passed"):
        return 1.0
    if result.get("failed"):
        return -1.0
    return 0.0
