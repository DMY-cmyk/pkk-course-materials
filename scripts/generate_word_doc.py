"""
generate_word_doc.py — Academic Report Word Document Generator
Usage: python scripts/generate_word_doc.py [--output PATH]

Output default: <project_root>/01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx
"""

import argparse
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from docx import Document
from scripts.word_doc.styles import setup_document, add_page_numbers, add_page_break
from scripts.word_doc.cover import build_cover
from scripts.word_doc.front_matter import build_front_matter
from scripts.word_doc.sections import (
    bagian_i, bagian_ii, bagian_iii, bagian_iv,
    bagian_v, bagian_vi, bagian_vii, bagian_viii,
)
from scripts.word_doc.bibliography import build_bibliography


def main(output_path: str) -> None:
    doc = Document()
    setup_document(doc)
    add_page_numbers(doc)

    logo_path = os.path.join(PROJECT_ROOT, "STIE Logo.png")
    bib_path = os.path.join(
        PROJECT_ROOT, "Daftar Pustaka — Presentasi Kelompok 3.txt"
    )

    print("[1/12] Cover page …")
    build_cover(doc, logo_path)
    add_page_break(doc)

    print("[2/12] Front matter (ToC + Kata Pengantar) …")
    build_front_matter(doc)

    print("[3/12] Bagian I — Konteks & Evolusi CF …")
    bagian_i.build(doc)
    add_page_break(doc)

    print("[4/12] Bagian II — Karakteristik Kualitatif …")
    bagian_ii.build(doc)
    add_page_break(doc)

    print("[5/12] Bagian III — Elemen LK …")
    bagian_iii.build(doc)
    add_page_break(doc)

    print("[6/12] Bagian IV — Pengakuan & Pengukuran …")
    bagian_iv.build(doc)
    add_page_break(doc)

    print("[7/12] Bagian V — Catatan Kritis …")
    bagian_v.build(doc)
    add_page_break(doc)

    print("[8/12] Bagian VI — Sintesis Teori …")
    bagian_vi.build(doc)
    add_page_break(doc)

    print("[9/12] Bagian VII — Studi Kasus INDF 2024 …")
    bagian_vii.build(doc)
    add_page_break(doc)

    print("[10/12] Bagian VIII — Kesimpulan …")
    bagian_viii.build(doc)

    print("[11/12] Daftar Pustaka …")
    build_bibliography(doc, bib_path)

    print(f"[12/12] Saving to: {output_path}")
    doc.save(output_path)
    print(f"Done. File: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Academic Report Word document")
    default_output = os.path.join(
        PROJECT_ROOT,
        "01079_Dzaki Muhammad Yusfian_Tugas Kelompok PKK.docx"
    )
    parser.add_argument("--output", default=default_output,
                        help="Output .docx file path")
    args = parser.parse_args()
    main(args.output)
