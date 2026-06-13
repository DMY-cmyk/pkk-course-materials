"""
extract_text.py — extracts Wolk Ch. 13 text per page and segments it by the
chapter's section headings; writes a verification report with per-page image
counts.

PyMuPDF (fitz) is the documented Python fallback for text extraction in this
otherwise-Rust pipeline: Rust lopdf.extract_text returns only page footers on
this SAGE-edition PDF (fonts lack ToUnicode CMaps), so it cannot read the body.
Consumes extraction/chapter-range.json (from the chapter_locator Rust crate).
"""
import json
import os
import sys

import fitz  # PyMuPDF

# Ordered top-level headings of Wolk Ch. 13 (SAGE edition) -> output slugs.
# Strings must match the exact text as it appears on a standalone line in the PDF.
# Tuned after inspecting extracted text in Step 5.
SECTIONS = [
    ("Learning Objectives", "01_learning_objectives"),
    ("The Statement of Changes in Financial Position", "02_scfp"),
    ("The Motivation for a Cash Flow Statement", "05_motivation"),
    ("Requirements of the Cash Flow Statement", "06_requirements"),
    ("The Nonarticulation Problem", "07_nonarticulation"),
    ("Classification Problems of SFAS No. 95", "08_classification"),
    ("Analytical Usefulness of the Cash Flow Statement", "09_analytical"),
    ("Issues Relating to Rules for Classifying Cash Flows", "09b_issues"),
    ("Cash Flow Needs of Different Users", "10_users"),
    ("Cash and Funds Flow Research", "11_research"),
    ("Improving the SCF", "12_improving"),
    ("Summary", "13_summary"),
    ("Questions", "14_questions"),
]


def segment(lines, sections):
    """Split `lines` (list of str) into [(slug, text)] at the first standalone
    occurrence of each heading, searching strictly forward so a heading phrase
    appearing in prose before its real heading does not cause a false cut.

    A line matches a heading when `line.strip() == heading`. Text before the
    first matched heading becomes the '00_preamble' segment. Returns [] if no
    heading matches at all.
    """
    cut_idx = []  # (line_index, slug)
    search_from = 0
    for heading, slug in sections:
        found = None
        for i in range(search_from, len(lines)):
            if lines[i].strip() == heading:
                found = i
                break
        if found is not None:
            cut_idx.append((found, slug))
            search_from = found + 1
    if not cut_idx:
        return []
    out = []
    first = cut_idx[0][0]
    if first > 0:
        out.append(("00_preamble", "\n".join(lines[:first])))
    for j, (start, slug) in enumerate(cut_idx):
        end = cut_idx[j + 1][0] if j + 1 < len(cut_idx) else len(lines)
        out.append((slug, "\n".join(lines[start:end])))
    return out


def page_numbers(text):
    """Extract sorted unique PDF page numbers from [[page:N]] markers in text."""
    nums = set()
    for piece in text.split("[[page:")[1:]:
        head = piece.split("]]", 1)[0]
        if head.isdigit():
            nums.add(int(head))
    return sorted(nums)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.normpath(os.path.join(here, "..", ".."))
    range_path = os.path.join(root, "extraction", "chapter-range.json")
    if not os.path.exists(range_path):
        sys.exit(f"missing {range_path} — run chapter_locator first")
    with open(range_path, encoding="utf-8") as f:
        rng = json.load(f)
    start, end = int(rng["start_page"]), int(rng["end_page"])

    pdf_path = os.path.join(
        root, "input", "chapter", "PKK Pert. 10 - Statement of Cashflow.pdf")
    doc = fitz.open(pdf_path)

    lines = []
    for p in range(start, end + 1):
        lines.append(f"[[page:{p}]]")
        page_text = doc[p - 1].get_text()
        lines.extend(page_text.splitlines())
    if not "".join(lines).strip():
        sys.exit("extracted chapter text is empty — extraction failed")

    segs = segment(lines, SECTIONS)
    matched = max(len(segs) - 1, 0)  # minus preamble
    if matched < 4:
        sys.exit(f"only {matched} of {len(SECTIONS)} headings matched — inspect extraction")

    out_dir = os.path.join(root, "extraction", "text")
    os.makedirs(out_dir, exist_ok=True)
    page_map = {}
    for slug, body in segs:
        with open(os.path.join(out_dir, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(body)
        page_map[slug] = page_numbers(body)
    with open(os.path.join(root, "extraction", "page-map.json"), "w", encoding="utf-8") as f:
        json.dump(page_map, f, indent=2)

    # Verification report — image counts per page (do NOT assert zero; this chapter may have figures)
    rpt = ["# Verification report — exhibit presence, Wolk Ch. 13 (SAGE edition)\n",
           "| PDF page | image count |", "|---|---|"]
    total = 0
    for p in range(start, end + 1):
        n = len(doc[p - 1].get_images(full=True))
        total += n
        rpt.append(f"| {p} | {n} |")
    rpt.append(f"\n**Total images: {total}.**")
    with open(os.path.join(root, "extraction", "verification-report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(rpt))

    print(f"wrote {len(segs)} segment files, page-map.json, "
          f"verification-report.md (total images: {total})")


if __name__ == "__main__":
    main()
