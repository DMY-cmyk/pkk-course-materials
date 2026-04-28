"""Phase 1: extract per-page text and role hints from the deck PDF."""
from __future__ import annotations
import json
import re
from pathlib import Path
from pypdf import PdfReader

PDF_PATH = Path(
    r"d:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/"
    r"Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3.pdf"
)
OUT_PATH = Path(__file__).parent / "pages_raw.json"

ROLE_KEYWORDS = {
    "cover":   [r"\bcover\b", r"kelompok\s*3", r"pelaporan\s*keuangan\s*korporat"],
    "agenda":  [r"\bagenda\b", r"daftar\s*isi", r"outline"],
    "divider": [r"^\s*bagian\s*\d", r"^\s*part\s*\d", r"^\s*chapter\s*\d"],
    "qanda":   [r"q\s*&\s*a", r"tanya\s*jawab", r"pertanyaan"],
    "ending":  [r"terima\s*kasih", r"thank\s*you", r"daftar\s*pustaka", r"referensi"],
    "case":    [r"indofood", r"\bindf\b", r"studi\s*kasus"],
    "chart":   [r"grafik", r"chart", r"diagram"],
    "table":   [r"tabel", r"\btable\b"],
}

def classify(text: str) -> str:
    low = text.lower()
    for role, patterns in ROLE_KEYWORDS.items():
        if any(re.search(p, low) for p in patterns):
            return role
    word_count = len(low.split())
    if word_count < 12:
        return "divider"
    return "content"

def extract():
    reader = PdfReader(str(PDF_PATH))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()
        pages.append({
            "page": i,
            "total": len(reader.pages),
            "text": text,
            "word_count": len(text.split()),
            "role_hint": classify(text),
        })
    OUT_PATH.write_text(
        json.dumps(pages, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {len(pages)} pages to {OUT_PATH}")

if __name__ == "__main__":
    extract()
