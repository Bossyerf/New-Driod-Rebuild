import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_DIR = os.getenv("CHROMA_DIR", ".chroma")
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "please_change_me")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
PRIMARY_MODEL = os.getenv("PRIMARY_MODEL", "qwen3:vl")
FALLBACK_MODEL = os.getenv("FALLBACK_MODEL", "qwen2.5:vl")
UE_SOURCE_ROOT = os.getenv("UE_SOURCE_ROOT", "E:\\UeSource")
