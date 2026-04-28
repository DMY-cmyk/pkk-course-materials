"""Phase 2 prep: build empty narration skeleton from raw extraction."""
import json
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "pages_raw.json"
OUT = HERE / "pages_narration.json"

raw = json.loads(RAW.read_text(encoding="utf-8"))
skeleton = []
for r in raw:
    skeleton.append({
        "page": r["page"],
        "total": r["total"],
        "role": r["role_hint"],
        "title": "",
        "narration": "",
        "key_terms": [],
    })
OUT.write_text(json.dumps(skeleton, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Initialized {len(skeleton)} empty narration entries at {OUT}")
