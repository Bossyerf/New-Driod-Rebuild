from typing import Dict, Any

# TODO: implement episode storage and reward shaping

def step(task: str, result: Dict[str, Any]) -> float:
    # return a placeholder reward
    return 1.0 if result.get("passed") else -1.0
