from typing import Dict, Any, List

class EpisodeStore:
    def __init__(self) -> void:
        self.episodes: List[Dict[str, Any]] = []

    def add(self, task: str, result: Dict[str, Any], reward: float) -> None:
        self.episodes.append({"task": task, "result": result, "reward": reward})

    def all(self) -> List[Dict[str, Any]]:
        return list(self.episodes)
