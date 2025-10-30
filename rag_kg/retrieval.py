from typing import List
from .config import CHROMA_DIR, NEO4J_URI

# TODO: integrate Chroma + Neo4j; current function returns placeholder context

def retrieve(query: str) -> List[str]:
    return [f"context(chroma={CHROMA_DIR}, neo4j={NEO4J_URI}) for: {query}"]
