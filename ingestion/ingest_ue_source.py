import os
import json
from pathlib import Path

UE_ROOT = os.environ.get("UE_SOURCE_ROOT", "E:\\UeSource")

# TODO: chunk UE source safely (filter large/binary) and index to Chroma + Neo4j

def main():
    out = Path(".chroma")
    out.mkdir(exist_ok=True)
    (out / "ue_source_placeholders.json").write_text(json.dumps({"ok": True, "root": UE_ROOT}))
    print(f"UE source indexed (placeholder) from {UE_ROOT}")

if __name__ == "__main__":
    main()
