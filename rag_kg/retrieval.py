from typing import List

# TODO: wire Chroma + Neo4j. Expose retrieve(query) that merges vector + graph.

def retrieve(query: str) -> List[str]:
    return [f"placeholder-context-for: {query}"]
