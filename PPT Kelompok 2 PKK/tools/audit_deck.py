"""Audit gate for the RMK-aligned deck revision (spec 2026-06-06).

Checks, against `Statement of Cash Flows.html`:
  1. data-label sequence == the approved 23-slide structure (strict RMK order)
  2. every ghost/pnum slide number matches its 1-based slide position
  3. REQUIRED content markers present (error fixes + gap fills)
  4. FORBIDDEN content markers absent (the confirmed factual errors)
Exit 0 = all gates pass.
"""
import pathlib
import re
import sys

DECK = pathlib.Path(__file__).resolve().parents[1] / "Statement of Cash Flows.html"

EXPECTED_LABELS = [
    "Judul",
    "Pendahuluan",
    "SCFP Sources & Uses",
    "Definisi Dana",
    "Motivasi ke Kas",
    "Tujuan SCF",
    "Tiga Aktivitas",
    "Direct Method",
    "Indirect Method",
    "Nonartikulasi 3M",
    "Bunga & Dividen",
    "Premium Obligasi",
    "Ingram & Lee",
    "Misklasifikasi",
    "WorldCom Terlihat Sehat",
    "Minus 12,3 Miliar",
    "Buffett & Nilai Intrinsik",
    "Free Cash Flow",
    "ABC SCF ke FCF",
    "Empat Ukuran",
    "Riset Arus Kas",
    "Memperbaiki SCF",
    "Sintesis",
]

REQUIRED = [
    # slide 3 — SCFP
    "transaction credits = transaction debits",
    # slide 4 — fund definitions + timeline
    "quick assets",
    "APB Opinion No. 3",
    # slide 6 — objectives
    "Quality of income",
    "crude ranking of liquidity",
    # slide 8 — Exhibit 13.2 fixes
    "$600</td>",
    "$1,065",
    "Cash &amp; equivalents, end of year",
    # slide 9 — indirect enrichment
    "282 responden",
    "plug number",
    # slide 10 — nonarticulation causes
    "Bahnson",
    # slide 12 — premium methods corrected
    "pelunasan (2004)",
    "penerbitan (2000)",
    # slide 14 — misclassification
    "part of our core business",
    # slide 15 — WorldCom quote
    "ignore one or more parts",
    # slide 17 — Buffett
    "NPV positif",
    # slide 18 — FCF definition
    "absence of a superior claim",
    # slide 20 — four measures guidance
    "WACC",
    # slide 21 — research section
    "Profit is an abstraction",
    "Lawson",
    # slide 22 — Broome
    "Broome",
]

FORBIDDEN = [
    # confirmed factual errors (spec section "Confirmed factual errors")
    "$6,001",
    "Net increase in cash &amp; equivalents</td><td>$1,665",
    # old, wrong premium-method texts
    "Seluruh penerimaan obligasi",
    "Amortisasi premium mengurangi",
    # Winston-framing slides removed per user decision
    'data-label="Janji Pembuka"',
    'data-label="Kontribusi"',
]


def main() -> int:
    text = DECK.read_text(encoding="utf-8")
    errors = []

    labels = re.findall(r'data-label="([^"]+)"', text)
    if labels != EXPECTED_LABELS:
        errors.append(
            "label sequence mismatch:\n    got      = %r\n    expected = %r"
            % (labels, EXPECTED_LABELS)
        )

    # ghost / pnum numbers must equal the slide's 1-based position
    sections = text.split("<section")[1:]
    for i, chunk in enumerate(sections, start=1):
        for kind, num in re.findall(
            r'class="(ghost[^"]*|pnum)"[^>]*>\s*(\d+)\s*<', chunk
        ):
            if int(num) != i:
                errors.append(
                    "slide %d (%s): %s shows %s, expected %02d"
                    % (i, labels[i - 1] if i <= len(labels) else "?", kind, num, i)
                )

    for marker in REQUIRED:
        if marker not in text:
            errors.append("missing required marker: %r" % marker)

    for marker in FORBIDDEN:
        if marker in text:
            errors.append("forbidden marker present: %r" % marker)

    if errors:
        print("AUDIT: FAIL (%d issue(s))" % len(errors))
        for e in errors:
            print("  - " + e)
        return 1
    print("AUDIT: PASS — %d slides, all gates green" % len(labels))
    return 0


if __name__ == "__main__":
    sys.exit(main())
