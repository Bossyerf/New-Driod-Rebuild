import os
import json
from pathlib import Path

# TODO: implement real docs crawling/parsing; this emits placeholders

def main():
    out = Path(".chroma")
    out.mkdir(exist_ok=True)
    (out / "docs_placeholders.json").write_text(json.dumps({"ok": True}))
    print("Docs ingested (placeholder)")

if __name__ == "__main__":
    main()
