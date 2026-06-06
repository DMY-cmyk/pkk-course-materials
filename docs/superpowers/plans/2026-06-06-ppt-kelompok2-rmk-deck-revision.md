# PPT Kelompok 2 PKK — RMK-Aligned Deck Revision Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Revise `PPT Kelompok 2 PKK/Statement of Cash Flows.html` from 19 to 23 slides in strict RMK section order, fixing two confirmed factual errors and filling all RMK coverage gaps, per the approved spec `docs/superpowers/specs/2026-06-06-ppt-kelompok2-rmk-revision-design.md`.

**Architecture:** Single self-contained HTML deck driven by the `<deck-stage>` web component. All revision happens inside the `<deck-stage>` body of one file; `deck.css`, `deck-stage.js`, fonts, and assets are NOT modified. A Python audit script (stdlib-only) acts as the test suite: it asserts the exact 23-label sequence, ghost/page-number correctness, presence of required content markers, and absence of known-wrong content. Tasks proceed top-to-bottom through the file so each Edit anchor stays unique and stable.

**Tech Stack:** HTML/CSS (existing design system classes only: `.bg/.blob`, `.pill`, `.ghost`, `.sidepanel/.pnum/.capsule/.vtext`, `.slide`, `.display/.subhead/.kicker/.body`, `ul.bul`, `.gcards/.gcard`, `.statgrid/.stat`, `.exhibit/table.fin`, `.bigstat`, `.anim d1–d5`), Python 3 for the audit script.

**Authoritative content source:** `pkk-rmk-cash-flows-kelompok2/content/sections/*.md` + `content/figures/` (the validated build input of the RMK docx). Never introduce content from outside these files.

**Working conventions for every task:**
- The deck file is `PPT Kelompok 2 PKK/Statement of Cash Flows.html` (call it DECK below). Read the relevant region before editing.
- "Replace block X" means: replace everything from the HTML comment that opens the block through the matching closing `</section>` (inclusive of the comment), with the given new content. Comments in the file look like `<!-- ============ SLIDE N — NAME ============ -->` and are unique anchors.
- After every task: run `python "PPT Kelompok 2 PKK/tools/audit_deck.py"` and confirm the failures remaining are only the ones listed for that task, then commit with the given message.
- All slide text is Bahasa Indonesia, S2 professor register, faithful to the RMK. Do not invent numbers or sources.

---

### Task 1: Audit script (the failing test)

**Files:**
- Create: `PPT Kelompok 2 PKK/tools/audit_deck.py`

- [ ] **Step 1: Write the audit script**

```python
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
```

- [ ] **Step 2: Run it to verify it fails (deck is still the 19-slide original)**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: `AUDIT: FAIL` with (at minimum) the label-sequence mismatch, ~20 missing REQUIRED markers, and 6 forbidden markers present (`$6,001`, the `$1,665` mislabel, both old premium texts, both old data-labels).

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/tools/audit_deck.py"
git commit -m "test(ppt-k2): audit gate for RMK-aligned deck revision (RED)"
```

---

### Task 2: Slide 2 "Pendahuluan" (replaces old slides 2 AND 3)

Old slide 2 (Janji Pembuka) and old slide 3 (Visi SCFP ke SCF) are both removed; one new Pendahuluan slide takes their place. Source: `content/sections/00-pendahuluan.md`.

**Files:**
- Modify: `PPT Kelompok 2 PKK/Statement of Cash Flows.html` (block between the SLIDE 2 comment and the SLIDE 4 comment)

- [ ] **Step 1: Replace the block** starting at `<!-- ============ SLIDE 2 — JANJI PEMBUKA ============ -->` and ending with the `</section>` of old slide 3 (i.e., everything before `<!-- ============ SLIDE 4 — SCFP SOURCES & USES ============ -->`) with:

```html
  <!-- ============ SLIDE 2 — PENDAHULUAN ============ -->
  <section data-label="Pendahuluan">
    <div class="bg bg-soft">
      <div class="blob b-blue b1"></div>
      <div class="blob b-warm b4"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="pill"></div>
    <div class="ghost br" style="bottom:-120px;">02</div>
    <div class="slide" style="flex-direction:row; align-items:center; gap:90px; justify-content:space-between;">
      <div style="max-width:680px;">
        <h2 class="display h-m anim">Kas, bukan laba,<br>yang membayar tagihan</h2>
        <p class="kicker anim d1" style="margin:30px 0 22px; font-size:21px;">Pendahuluan — “Cash for the merchandise…”</p>
        <p class="body anim d2">Adegan pembuka <em>The Music Man</em> memuat tesis akuntansi paling mendasar: tagihan, investasi, utang, dan dividen pada akhirnya dibayar dengan <strong>kas, bukan laba</strong>. Perusahaan yang gagal menghasilkan kas yang cukup menghadapi kepunahan. Yang tidak sederhana: cara terbaik menyampaikan arus kas historis kepada pengguna laporan.</p>
      </div>
      <div class="gcards anim d2">
        <div class="gcard"><span class="gn">01</span><span class="gt"><strong>1971 — APB Opinion No. 19</strong>: SCFP (“funds flow”) diwajibkan</span></div>
        <div class="gcard"><span class="gn">02</span><span class="gt"><strong>1987 — SFAS No. 95</strong>: SCF berbasis kas menggantikan SCFP</span></div>
        <div class="gcard"><span class="gn">03</span><span class="gt">Alur bab: SCFP → tujuan → struktur → nonartikulasi &amp; klasifikasi → FCF → riset → perbaikan</span></div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL, but `data-label="Janji Pembuka"` no longer listed as forbidden-present; label list now starts `["Judul", "Pendahuluan", "SCFP Sources & Uses", ...]`.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): slide 2 Pendahuluan replaces promise+visi slides (RMK 00)"
```

---

### Task 3: Slide 3 "SCFP Sources & Uses" (edit old slide 4)

Source: `content/sections/01-scfp-funds-flow.md` (+ eq-13-1 and Exhibit 13.1 already on the slide).

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 4 — SCFP SOURCES & USES ============ -->`

- [ ] **Step 1: Replace the block** (through its `</section>`) with:

```html
  <!-- ============ SLIDE 3 — SCFP SOURCES & USES ============ -->
  <section data-label="SCFP Sources & Uses">
    <div class="bg bg-soft">
      <div class="blob b-warm" style="width:420px;height:340px;left:-130px;top:-120px;opacity:.5;"></div>
      <div class="blob b-blue b1" style="left:60px;"></div>
      <div class="blob b-blue-d" style="width:720px;height:600px;right:-240px;bottom:-240px;opacity:.75;"></div>
    </div>
    <div class="ghost br" style="bottom:-110px;">03</div>
    <div class="slide" style="flex-direction:row; gap:80px; justify-content:space-between; align-items:center;">
      <div style="max-width:620px;">
        <h2 class="display h-m anim">SCFP:<br>Sources &amp; Uses</h2>
        <p class="kicker anim d1" style="margin:30px 0 12px; font-size:22px;">Identitas (13.1)</p>
        <p class="subhead sm anim d1" style="margin:0 0 26px; font-size:26px; color:var(--blue-900);">transaction credits = transaction debits</p>
        <ul class="bul anim d2">
          <li><strong>Sources</strong> (credits): kenaikan ekuitas, penurunan aset · <strong>Uses</strong> (debits): kebalikannya</li>
          <li>Tiga tujuan APB No. 19: melengkapi pengungkapan; meringkas pendanaan &amp; investasi; melaporkan <em>funds flow</em> operasi</li>
          <li>Laporan <strong>derivatif</strong> — menyusun ulang data laba rugi &amp; neraca, tanpa pengukuran baru</li>
          <li><em>All-inclusive</em>: butir 2 menangkap transaksi nonfund (konversi utang, saham untuk aset, dividen properti)</li>
        </ul>
      </div>
      <div class="exhibit anim d3" style="width:560px;">
        <div class="ex-title">Exhibit 13.1 — Standard Format of the Statement of Changes in Financial Position</div>
        <div style="font-size:15px; color:var(--ink); line-height:1.5;">
          <p style="font-weight:700; margin:4px 0 6px; color:var(--blue-700);">Sources of Resources <span style="font-weight:400;color:var(--ink-faint)">(transaction credits)</span></p>
          <ol style="margin:0 0 14px; padding-left:22px; color:var(--ink-soft);">
            <li>Increases to the “fund balance” accounts
              <div style="padding-left:8px;">a. From net income<br>b. From other sources</div></li>
            <li>Other sources of resources</li>
            <li>Decrease, if any, in the fund balance for the period</li>
          </ol>
          <p style="font-weight:700; margin:4px 0 6px; color:var(--blue-700);">Uses of Resources <span style="font-weight:400;color:var(--ink-faint)">(transaction debits)</span></p>
          <ol style="margin:0; padding-left:22px; color:var(--ink-soft);">
            <li>Decreases to the “fund balance” accounts
              <div style="padding-left:8px;">a. From net losses<br>b. From other sources</div></li>
            <li>Other uses of resources</li>
            <li>Increase, if any, in the fund balance for the period</li>
          </ol>
        </div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL, but required marker `transaction credits = transaction debits` is now satisfied.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): slide 3 SCFP adds eq 13.1 + APB 19 objectives (RMK 01)"
```

---

### Task 4: Slide 4 "Definisi Dana" (NEW — insert after slide 3)

Source: `content/sections/01-scfp-funds-flow.md` (four fund definitions, cost rationale, 1963/1971 timeline).

**Files:**
- Modify: DECK — insert directly after the `</section>` of slide 3 (before `<!-- ============ SLIDE 5 — MOTIVASI & TUJUAN (section) ============ -->`)

- [ ] **Step 1: Insert this block**

```html

  <!-- ============ SLIDE 4 — DEFINISI DANA & GARIS WAKTU ============ -->
  <section data-label="Definisi Dana">
    <div class="bg bg-soft">
      <div class="blob b-blue b3"></div>
      <div class="blob b-warm" style="width:360px;height:300px;left:120px;top:-100px;opacity:.4;"></div>
    </div>
    <div class="sidepanel left" style="width:300px;">
      <div class="pnum" style="top:-30px; left:14px; font-size:300px;">04</div>
      <div class="capsule" style="left:64px; top:330px; width:64px; height:430px;"></div>
    </div>
    <div class="slide" style="padding-left:420px; justify-content:center;">
      <div class="statgrid anim" style="margin-bottom:70px;">
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">01</span><span class="txt">Empat definisi dana: kas · kas + <em>near cash</em> · <em>quick assets</em> · modal kerja</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">02</span><span class="txt">Modal kerja meminimalkan item nonfund → pilihan mayoritas (alasan biaya)</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">03</span><span class="txt"><strong style="color:var(--ink)">1963 — APB Opinion No. 3</strong>: dianjurkan · <strong style="color:var(--ink)">1971 — SEC</strong>: wajib untuk <em>statutory filings</em></span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">04</span><span class="txt"><strong style="color:var(--ink)">1971 — APB Opinion No. 19</strong>: SCFP wajib bagi seluruh pelaporan keuangan</span></div></div>
      </div>
      <h2 class="display h-m anim d2" style="max-width:820px;">Empat definisi dana,<br>satu pilihan ekonomis</h2>
      <p class="subhead sm anim d3" style="margin-top:30px; color:var(--ink-soft);">Fleksibilitas APB No. 19 — regulator yang mengakselerasi adopsi</p>
    </div>
  </section>
```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL, but `quick assets` and `APB Opinion No. 3` markers satisfied; label list now `[..., "SCFP Sources & Uses", "Definisi Dana", "Motivasi & Tujuan SCF", ...]`.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): new slide 4 fund definitions + adoption timeline (RMK 01)"
```

---

### Task 5: Slides 5–6 "Motivasi ke Kas" + "Tujuan SCF" (split old slide 5)

Sources: `content/sections/02-motivation-scf.md`, `content/sections/03-objectives.md`.

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 5 — MOTIVASI & TUJUAN (section) ============ -->`

- [ ] **Step 1: Replace the block** (through its `</section>`) with these TWO sections:

```html
  <!-- ============ SLIDE 5 — MOTIVASI KE KAS ============ -->
  <section data-label="Motivasi ke Kas">
    <div class="bg bg-soft">
      <div class="blob b-blue b3"></div>
      <div class="blob b-warm" style="width:360px;height:300px;left:120px;top:-100px;opacity:.4;"></div>
    </div>
    <div class="sidepanel left" style="width:300px;">
      <div class="pnum" style="top:-30px; left:30px; font-size:300px;">05</div>
      <div class="capsule" style="left:64px; top:330px; width:64px; height:430px;"></div>
    </div>
    <div class="slide" style="padding-left:420px; justify-content:center;">
      <div class="statgrid anim" style="margin-bottom:70px;">
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">01</span><span class="txt"><em>Deferred charges &amp; credits</em> ikut dihitung — tanpa konsekuensi arus kas</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">02</span><span class="txt">Konversi aset lancar bisa &gt;1 tahun — siklus operasi yang panjang</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">03</span><span class="txt">Persediaan dicatat atas dasar biaya — bukan potensi kas nyata</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">04</span><span class="txt">Konsensus FASB: dana = <strong style="color:var(--ink)">kas</strong> — “cash is cash is cash”</span></div></div>
      </div>
      <h2 class="display h-m anim d2" style="max-width:760px;">Mengapa kas,<br>bukan modal kerja?</h2>
      <p class="subhead sm anim d3" style="margin-top:30px; color:var(--ink-soft);">Net working capital gagal sebagai ukuran likuiditas</p>
    </div>
  </section>

  <!-- ============ SLIDE 6 — TUJUAN SCF ============ -->
  <section data-label="Tujuan SCF">
    <div class="bg bg-soft">
      <div class="blob b-blue b1"></div>
      <div class="blob b-warm b4"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="pill"></div>
    <div class="ghost tr blue" style="font-size:340px;">06</div>
    <div class="slide" style="justify-content:center;">
      <h2 class="display h-m anim" style="max-width:980px;">Untuk apa<br>laporan arus kas?</h2>
      <p class="subhead sm anim d1" style="margin:26px 0 14px; color:var(--ink);">SFAC No. 1 &amp; No. 5 — enam manfaat discussion memorandum</p>
      <p class="body anim d1" style="max-width:1120px; font-size:22px;">SFAC No. 1: informasi berguna bagi keputusan rasional — termasuk menilai arus kas masa depan. SFAC No. 5: menilai <strong>likuiditas, fleksibilitas, profitabilitas, dan risiko</strong>. Likuiditas ≠ fleksibilitas; klasifikasi lancar–tak lancar neraca hanyalah <strong>“crude ranking of liquidity”</strong>.</p>
      <div class="statgrid anim d2" style="grid-template-columns:repeat(3,1fr); gap:34px 56px; max-width:1380px; margin-top:46px;">
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">01</span><span class="txt">Umpan balik atas arus kas aktual</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">02</span><span class="txt">Hubungan laba akuntansi ↔ arus kas</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">03</span><span class="txt"><strong style="color:var(--ink)">Quality of income</strong> — korelasi laba dengan kas operasi</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">04</span><span class="txt">Komparabilitas — CFO tunduk pada lebih sedikit pilihan kebijakan</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">05</span><span class="txt">Menilai fleksibilitas &amp; likuiditas keuangan</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">06</span><span class="txt">Prediksi arus kas masa depan — filosofi <em>expanded disclosure</em></span></div></div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL, but `Quality of income` and `crude ranking of liquidity` satisfied; labels 1–7 now match EXPECTED_LABELS.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): split motivasi/tujuan; six DM benefits added (RMK 02-03)"
```

---

### Task 6: Slide 7 "Tiga Aktivitas" (edit old slide 6)

Source: `content/sections/04-structure-trichotomy.md`.

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 6 — STRUKTUR / TIGA AKTIVITAS (section) ============ -->`

- [ ] **Step 1: Replace the block** with:

```html
  <!-- ============ SLIDE 7 — TIGA AKTIVITAS ============ -->
  <section data-label="Tiga Aktivitas">
    <div class="bg bg-soft">
      <div class="blob b-blue b3"></div>
      <div class="blob b-warm" style="width:360px;height:300px;left:140px;top:-110px;opacity:.4;"></div>
    </div>
    <div class="sidepanel left" style="width:300px;">
      <div class="pnum" style="top:-30px; left:18px; font-size:300px;">07</div>
      <div class="capsule" style="left:64px; top:330px; width:64px; height:430px;"></div>
    </div>
    <div class="slide" style="padding-left:420px; justify-content:center;">
      <div class="statgrid anim" style="margin-bottom:70px;">
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">01</span><span class="txt"><strong style="color:var(--ink)">Operasi</strong> — kas dari bisnis inti</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">02</span><span class="txt"><strong style="color:var(--ink)">Investasi</strong> — perolehan &amp; pelepasan aset jangka panjang</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">03</span><span class="txt"><strong style="color:var(--ink)">Pendanaan</strong> — utang dan ekuitas</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">04</span><span class="txt">Kas = kas + <em>cash equivalents</em>; transaksi nonkas wajib diungkap suplemen</span></div></div>
      </div>
      <h2 class="display h-m anim d2" style="max-width:760px;">Tiga aktivitas,<br>satu cerita</h2>
      <p class="subhead sm anim d3" style="margin-top:30px; color:var(--ink-soft);">SFAS No. 95 — diadopsi dengan dissent 3 dari 7 anggota</p>
    </div>
  </section>
```

- [ ] **Step 2: Verify** with Grep on DECK: pattern `dissent 3 dari 7` → 1 match.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): slide 7 trichotomy + cash definition + dissent teaser (RMK 04)"
```

---

### Task 7: Slide 8 "Direct Method" — FIX THE FACTUAL ERRORS

Source: `content/sections/05-direct-vs-indirect.md` ¶ on Exhibit 13.2: facility sale **$600**; CFO 1,365 + CFI (1,175) + CFF 875 = **net increase $1,065**; beginning cash $600 → ending **$1,665**.

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 7 — DIRECT METHOD ============ -->`

- [ ] **Step 1:** In that block, update the comment line to `<!-- ============ SLIDE 8 — DIRECT METHOD ============ -->` and the ghost to `>08<`:

```html
    <div class="ghost br" style="bottom:-100px;">08</div>
```

- [ ] **Step 2: Fix the facility-sale row.** Replace:

```html
          <tr><td>Proceeds from sale of facility</td><td>$6,001</td></tr>
```

with:

```html
          <tr><td>Proceeds from sale of facility</td><td>$600</td></tr>
```

- [ ] **Step 3: Fix the bottom of the table.** Replace:

```html
          <tr class="grand"><td>Net increase in cash &amp; equivalents</td><td>$1,665</td></tr>
```

with:

```html
          <tr class="tot"><td>Net increase in cash &amp; equivalents</td><td>$1,065</td></tr>
          <tr class="grand"><td>Cash &amp; equivalents, end of year</td><td>$1,665</td></tr>
```

- [ ] **Step 4: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall, but `$6,001` and the `$1,665` mislabel gone from forbidden-present; `$600</td>`, `$1,065`, `Cash &amp; equivalents, end of year` satisfied.

- [ ] **Step 5: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "fix(ppt-k2): Exhibit 13.2 — facility sale \$600, net increase \$1,065 (RMK 05)"
```

---

### Task 8: Slide 9 "Indirect Method" (enrich old slide 8)

Source: `content/sections/05-direct-vs-indirect.md` (identical bottom line, plug number, McEnroe 282/56%).

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 8 — INDIRECT METHOD ============ -->`

- [ ] **Step 1:** Update comment to `SLIDE 9 — INDIRECT METHOD`, ghost to `>09<`, and replace the left-column `<ul class="bul ...">` with:

```html
        <ul class="bul anim d2" style="max-width:560px;">
          <li>Mulai dari <strong>net income</strong>, disesuaikan item nonkas — bermuara pada angka yang <strong>identik</strong>: $1,365</li>
          <li>Dipilih mayoritas perusahaan AS (alasan biaya); praktiknya kerap memuat <em>plug number</em> penyeimbang</li>
          <li>McEnroe — <strong>282 responden</strong>: 56% pengguna justru memilih direct method</li>
        </ul>
```

The exhibit table is verified correct — DO NOT touch it.

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `282 responden` and `plug number` satisfied.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): slide 9 indirect — identical bottom line, plug number, McEnroe n=282 (RMK 05)"
```

---

### Task 9: Slide 10 "Nonartikulasi 3M" (edit old slide 9)

Source: `content/sections/06-nonarticulation.md` (three causes, FASB–IASB 2008).

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 9 — NONARTIKULASI / 3M ============ -->`

- [ ] **Step 1:** Update comment to `SLIDE 10 — NONARTIKULASI / 3M`, ghost to `>10<`, and replace the `<ul class="bul ...">` with:

```html
      <ul class="bul anim d2" style="max-width:1060px; margin-bottom:30px;">
        <li>Penyesuaian modal kerja SCF ≠ perubahan neraca — <strong>75%</strong> sampel (Bahnson, Miller &amp; Budge); bahkan <strong>tanda</strong> pun bisa berbeda</li>
        <li>Tiga sebab: akuisisi tengah tahun · transaksi modal kerja nonkas (write-up persediaan, alokasi depresiasi, reklasifikasi) · satu akun AP untuk pembelian operasi &amp; investasi</li>
        <li>FASB–IASB 2008: klasifikasi gabungan “business” berpotensi menekan <em>classification shifting</em></li>
      </ul>
```

The Exhibit 13.4 table is verified correct — DO NOT touch it.

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `Bahnson` satisfied.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): slide 10 nonarticulation — three causes corrected + FASB-IASB 2008 (RMK 06)"
```

---

### Task 10: Slides 11–12 "Bunga & Dividen" + "Premium Obligasi" (edit old slides 10–11)

Source: `content/sections/07-classification-problems.md` (+ section 04 dissent).

**Files:**
- Modify: DECK, blocks `<!-- ============ SLIDE 10 — BUNGA & DIVIDEN (section) ============ -->` and `<!-- ============ SLIDE 11 — SATU PREMIUM, EMPAT CARA ============ -->`

- [ ] **Step 1:** In the Bunga & Dividen block: comment → `SLIDE 11 — BUNGA & DIVIDEN`, pnum → `>11<`, and replace the `statgrid` stats with:

```html
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">01</span><span class="txt">SFAS 95 ¶22–23: bunga &amp; dividen <strong style="color:var(--ink)">diterima</strong> = operasi; bunga <strong style="color:var(--ink)">dibayar</strong> = operasi — dissent 3/7: investasi &amp; pendanaan</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">02</span><span class="txt">Nurnberg: ditempatkan justru di kategori yang paling tidak mencerminkan hakikat ekonominya</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">03</span><span class="txt">Akar teori: <em>proprietary</em> (ikut laba rugi) vs <em>entity</em>; plus tekanan perbankan — hindari CFO negatif</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num">04</span><span class="txt">IAS 7: fleksibel asal konsisten → seragam intra-industri, tidak lintas-industri</span></div></div>
```

- [ ] **Step 2:** In the Premium block: comment → `SLIDE 12 — SATU PREMIUM, EMPAT CARA`, ghost → `>12<`, replace the intro `<p class="body anim d2" ...>` with:

```html
      <p class="body anim d2" style="max-width:1120px; margin-bottom:34px;">Obligasi kupon 8%, 4 tahun, nominal <strong>$10.000</strong>, terjual <strong>$11.000</strong> (31 Des 2000). Premi $1.000 diamortisasi garis lurus $250/tahun; beban bunga akrual <strong>$550</strong> = kupon $800 − amortisasi $250. Vent, Cowling &amp; Sevalstad menemukan empat metode dalam praktik.</p>
```

and replace the four `gcard` divs (inside the 4-column grid) with:

```html
        <div class="gcard" style="flex-direction:column; align-items:flex-start; min-height:220px; gap:14px;">
          <span class="gn">01</span><span class="gt">Premi → arus masuk <strong>pendanaan</strong> tahun 2000; operasi 2001–04 = $(800)/thn ≠ akrual $550.<br><em style="opacity:.85">Pilihan penulis ✓ — pasangan metode langsung</em></span>
        </div>
        <div class="gcard" style="flex-direction:column; align-items:flex-start; min-height:220px; gap:14px;">
          <span class="gn">02</span><span class="gt">Premi dipindahkan ke <strong>operasi</strong> pada tahun <strong>pelunasan (2004)</strong> — dimungkinkan di bawah metode tidak langsung.</span>
        </div>
        <div class="gcard" style="flex-direction:column; align-items:flex-start; min-height:220px; gap:14px;">
          <span class="gn">03</span><span class="gt">Premi dipindahkan ke <strong>operasi</strong> pada tahun <strong>penerbitan (2000)</strong> — konsisten dengan saat premi diterima.</span>
        </div>
        <div class="gcard" style="flex-direction:column; align-items:flex-start; min-height:220px; gap:14px;">
          <span class="gn">04</span><span class="gt">Premi disebar 4 tahun sebagai arus keluar <strong>pendanaan</strong>: $800/thn = operasi $(550) + pendanaan $(250).<br><em style="opacity:.85">Paling tidak masuk akal — penilaian penulis</em></span>
        </div>
```

and replace the closing `<p class="body anim d4" ...>` with:

```html
      <p class="body anim d4" style="max-width:1180px; margin-top:30px; font-size:22px;">Masalah alokasi yang sama: bunga dikapitalisasi (SFAS 34 — hakikat vs tujuan), lease (operating = operasi; capital = bunga operasi + pokok pendanaan), hedging (SFAS 104 — <strong>fineness</strong> vs komparabilitas). <span style="color:var(--ink-faint)">(Exhibit 13.5)</span></p>
```

- [ ] **Step 3: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `pelunasan (2004)` and `penerbitan (2000)` satisfied; forbidden `Seluruh penerimaan obligasi` and `Amortisasi premium mengurangi` gone.

- [ ] **Step 4: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "fix(ppt-k2): premium methods 2/3/4 corrected per Vent et al.; classification slide enriched (RMK 07)"
```

---

### Task 11: Slides 13–14 "Ingram & Lee" + "Misklasifikasi" (split old slide 12)

Sources: `content/sections/08-analytical-usefulness.md`, `content/sections/09-misclassification.md`.

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 12 — SURPRISE: INGRAM & LEE ============ -->`

- [ ] **Step 1: Replace the block** with these TWO sections:

```html
  <!-- ============ SLIDE 13 — INGRAM & LEE ============ -->
  <section data-label="Ingram & Lee">
    <div class="bg bg-soft">
      <div class="blob b-blue b1"></div>
      <div class="blob b-warm" style="width:380px;height:320px;left:-120px;top:160px;opacity:.45;"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="pill"></div>
    <div class="ghost tr blue" style="font-size:340px;">13</div>
    <div class="slide" style="flex-direction:row; gap:80px; justify-content:space-between; align-items:center;">
      <div style="max-width:640px;">
        <h2 class="display h-m anim" style="font-size:72px;">Sidik jari<br>siklus hidup</h2>
        <p class="subhead sm anim d1" style="margin:34px 0 22px; color:var(--ink);">Ingram &amp; Lee — ±1.000 firma, 1974–1992</p>
        <p class="body anim d2">Firma <strong>bertumbuh</strong>: laba naik, <strong>CFO justru turun</strong> — piutang &amp; persediaan membengkak melebihi imbangan utang usaha.</p>
      </div>
      <div class="gcards anim d2">
        <div class="gcard"><span class="gn">01</span><span class="gt"><strong>Bertumbuh</strong>: investasi keluar besar, pendanaan masuk, dividen rendah — <em>leverage</em> lebih tinggi</span></div>
        <div class="gcard"><span class="gn">02</span><span class="gt"><strong>Berkontraksi</strong>: laba turun tapi CFO naik — kas terbebaskan; distribusi meningkat</span></div>
        <div class="gcard"><span class="gn">03</span><span class="gt">Pola lintas-seksi = sinyal vital — maka timbul insentif merekayasanya</span></div>
      </div>
    </div>
  </section>

  <!-- ============ SLIDE 14 — MISKLASIFIKASI ============ -->
  <section data-label="Misklasifikasi">
    <div class="bg bg-soft">
      <div class="blob b-warm" style="width:420px;height:340px;left:-140px;top:-130px;opacity:.5;"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="ghost br" style="bottom:-110px;">14</div>
    <div class="slide" style="flex-direction:row; gap:80px; justify-content:space-between; align-items:center;">
      <div style="max-width:640px;">
        <h2 class="display h-m anim" style="font-size:72px;">Menggeser kategori,<br>bukan kas</h2>
        <p class="subhead sm anim d1" style="margin:34px 0 22px; color:var(--ink);">Misklasifikasi — CFO dipoles tanpa mengubah total kas</p>
        <p class="body anim d2">Arus keluar digeser operasi→investasi, arus masuk digeser investasi→operasi. Aturan tak dilanggar secara formal — namun komparabilitas antarperusahaan paling banter menjadi lemah.</p>
      </div>
      <div class="gcards anim d2">
        <div class="gcard"><span class="gn">01</span><span class="gt"><strong>Tyco</strong>: kontrak dealer dicatat sebagai “akuisisi” — arus keluar operasi diakui jauh lebih lambat</span></div>
        <div class="gcard"><span class="gn">02</span><span class="gt"><strong>Ford/GM/Harley</strong>: notes receivable dealer = investasi; GM: CFO $7,6 M vs $3,5 M</span></div>
        <div class="gcard"><span class="gn">03</span><span class="gt"><strong>Navistar</strong>: reklasifikasi ke operasi — Oberle: “…part of our core business.”</span></div>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `part of our core business` satisfied.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): split lifecycle/misclassification slides; contraction symmetry + Navistar quote (RMK 08-09)"
```

---

### Task 12: Slides 15–16 WorldCom + −$12,3 M (light edits of old slides 13–14)

Source: `content/sections/10-scf-more-than-cfo.md`. Tables verified — DO NOT touch Exhibit 13.6.

**Files:**
- Modify: DECK, blocks `<!-- ============ SLIDE 13 — WORLDCOM TERLIHAT SEHAT ============ -->` and `<!-- ============ SLIDE 14 — -$12,3 MILIAR (big stat) ============ -->`

- [ ] **Step 1:** WorldCom block: comment → `SLIDE 15 — WORLDCOM TERLIHAT SEHAT`, ghost → `>15<`, and replace its `<ul class="bul ...">` with:

```html
      <ul class="bul anim d2" style="max-width:1060px; margin-bottom:30px;">
        <li>Laba bersih positif <strong>tiga tahun beruntun</strong>; beban operasi dikapitalisasi → CFO tampak kuat</li>
        <li>21 Juli 2002: petisi <strong>Chapter 11</strong> — padahal SCF utuh sudah memberi petunjuk</li>
        <li>“Investors who <strong>ignore one or more parts</strong> do so at their peril.” — Wolk, Dodd &amp; Rozycki</li>
      </ul>
```

- [ ] **Step 2:** −$12,3 M block: comment → `SLIDE 16 — MINUS 12,3 MILIAR`, pnum → `>16<`, and replace its `<ul class="bul ...">` with:

```html
      <ul class="bul anim d4" style="max-width:860px;">
        <li>CFO − CFI negatif pada <strong>3 dari 4</strong> tahun terakhir</li>
        <li>Pertanyaan analitisnya: berapa lama pola ini dapat berlanjut — dan bagaimana memanjat keluar?</li>
        <li>Pelajaran: jangan baca CFO saja — tiga bagian SCF satu kesatuan</li>
      </ul>
```

- [ ] **Step 3: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `ignore one or more parts` satisfied.

- [ ] **Step 4: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): WorldCom peril quote + how-long question (RMK 10)"
```

---

### Task 13: Slides 17–18 "Buffett & Nilai Intrinsik" + "Free Cash Flow" (split old slide 15)

Sources: `content/sections/11-user-needs.md`, `content/sections/12-free-cash-flow.md`.

**Files:**
- Modify: DECK, block `<!-- ============ SLIDE 15 — FREE CASH FLOW ============ -->`

- [ ] **Step 1: Replace the block** with these TWO sections:

```html
  <!-- ============ SLIDE 17 — BUFFETT & NILAI INTRINSIK ============ -->
  <section data-label="Buffett & Nilai Intrinsik">
    <div class="bg bg-soft">
      <div class="blob b-blue b1"></div>
      <div class="blob b-warm" style="width:380px;height:320px;left:-120px;top:160px;opacity:.45;"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="pill"></div>
    <div class="ghost tr blue" style="font-size:340px;">17</div>
    <div class="slide" style="flex-direction:row; gap:80px; justify-content:space-between; align-items:center;">
      <div style="max-width:640px;">
        <h2 class="display h-m anim" style="font-size:72px;">Tiga pertanyaan<br>Buffett</h2>
        <p class="subhead sm anim d1" style="margin:34px 0 22px; color:var(--ink);">Kebutuhan pengguna — surat BRKA 1988</p>
        <p class="body anim d2">Investasi = keputusan alokasi modal: terima bila <strong>NPV positif</strong>. Saham layak dibeli bila <strong>nilai intrinsik</strong> &gt; harga pasar — nilai diskonto kas yang dapat diambil selama sisa umur bisnis; sebuah <em>estimasi</em>, bukan presisi.</p>
      </div>
      <div class="gcards anim d2">
        <div class="gcard"><span class="gn">01</span><span class="gt">Berapa kira-kira <strong>nilai</strong> perusahaan ini? → valuation</span></div>
        <div class="gcard"><span class="gn">02</span><span class="gt">Mampukah memenuhi <strong>kewajiban</strong> masa depannya? → keputusan kredit</span></div>
        <div class="gcard"><span class="gn">03</span><span class="gt">Seberapa baik kerja <strong>manajemennya</strong>? → stewardship</span></div>
      </div>
    </div>
  </section>

  <!-- ============ SLIDE 18 — FREE CASH FLOW ============ -->
  <section data-label="Free Cash Flow">
    <div class="bg bg-soft">
      <div class="blob b-warm" style="width:420px;height:340px;left:-140px;top:-130px;opacity:.5;"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="ghost br" style="bottom:-100px;">18</div>
    <div class="slide" style="flex-direction:row; gap:80px; justify-content:space-between; align-items:center;">
      <div style="max-width:620px;">
        <h2 class="display h-l anim" style="font-size:100px; line-height:.9;">Free<br>Cash Flow</h2>
        <p class="kicker anim d1" style="margin:28px 0 26px; font-size:20px; max-width:560px;">Persamaan (13.2): FCF = NOPLAT − investasi pada operating invested capital</p>
        <ul class="bul anim d2" style="max-width:560px;">
          <li>“Free” = <em>absence of a superior claim</em> (Mulford &amp; Comiskey) — kas tanpa klaim yang lebih senior</li>
          <li><em>Entity theory</em> → <strong>cash flow to the firm</strong>; tidak tersedia langsung dari SCF</li>
          <li>Beban bunga <strong>tidak termasuk</strong> (beban pendanaan); kas operasi bagian dari <em>net operating working capital</em></li>
        </ul>
      </div>
      <div class="exhibit anim d3" style="width:560px; padding:34px 38px;">
        <div class="ex-title" style="border:none; padding:0; margin-bottom:24px; font-size:19px;">Anatomi Free Cash Flow</div>
        <div style="display:flex; flex-direction:column; gap:0;">
          <div style="display:flex; justify-content:space-between; align-items:center; padding:16px 0; border-bottom:1px solid var(--line);">
            <span style="font-size:19px; font-weight:700; color:var(--ink);">NOPLAT</span>
            <span style="font-size:15px; color:var(--ink-soft); text-align:right; max-width:300px;">Net operating profit less adjusted taxes — laba operasi setelah pajak, sebelum beban bunga</span>
          </div>
          <div style="display:flex; justify-content:center; padding:8px 0;"><span style="font-family:var(--font-mono); font-size:30px; color:var(--blue-700);">−</span></div>
          <div style="display:flex; justify-content:space-between; align-items:center; padding:16px 0; border-bottom:1px solid var(--line);">
            <span style="font-size:19px; font-weight:700; color:var(--ink);">Investasi pada<br>Operating Capital</span>
            <span style="font-size:15px; color:var(--ink-soft); text-align:right; max-width:300px;">Net operating working capital (termasuk kas operasi) + aset tak lancar</span>
          </div>
          <div style="display:flex; justify-content:center; padding:8px 0;"><span style="font-family:var(--font-mono); font-size:30px; color:var(--blue-700);">=</span></div>
          <div style="display:flex; justify-content:space-between; align-items:center; padding:18px 24px; border-radius:6px; background:var(--grad); color:#fff;">
            <span style="font-size:21px; font-weight:800;">FREE CASH FLOW</span>
            <span style="font-size:14px; max-width:230px; text-align:right; opacity:.92;">Kas bebas untuk kreditur &amp; pemegang saham</span>
          </div>
        </div>
        <p class="ex-src" style="margin-top:18px;">Konteks: Exhibit 13.7 — income statement &amp; balance sheet ABC Company.</p>
      </div>
    </div>
  </section>
```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `NPV positif` and `absence of a superior claim` satisfied.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): split Buffett/user-needs from FCF; superior-claim definition (RMK 11-12)"
```

---

### Task 14: Slides 19–20 ABC + Empat Ukuran (edit old slides 16–17)

Source: `content/sections/12-free-cash-flow.md`. All four tables verified — DO NOT change any numbers.

**Files:**
- Modify: DECK, blocks `<!-- ============ SLIDE 16 — ABC: DARI SCF KE FCF ============ -->` and `<!-- ============ SLIDE 17 — EMPAT UKURAN, EMPAT CERITA ============ -->`

- [ ] **Step 1:** ABC block: comment → `SLIDE 19 — ABC: DARI SCF KE FCF`; replace its `<ul class="bul ...">` with:

```html
        <ul class="bul anim d2">
          <li>CFO: <strong>$527 → $466 → $434</strong> (2005–2007)</li>
          <li>FCF: <strong>$332 → $99 → $80</strong> — cerita berbeda dari laba yang stabil</li>
          <li>Penurunan FCF bukan operasi memburuk — <strong>investasi makin agresif</strong>: $(277) → $(360)</li>
        </ul>
```

- [ ] **Step 2:** Empat Ukuran block: comment → `SLIDE 20 — EMPAT UKURAN, EMPAT CERITA`, ghost → `>20<`; replace its `<ul class="bul ...">` with:

```html
      <ul class="bul anim d2" style="max-width:1240px; margin-bottom:30px;">
        <li>FCF = CFO + bunga setelah pajak − kenaikan kas operasi − CFI</li>
        <li>Pilihan bergantung <strong>waktu, sumber daya, tujuan</strong>: NI = cepat · CFO = kualitas laba · CFO−CFI = anti-kapitalisasi beban · FCF = paling murni → dasar DCF dengan <strong>WACC</strong></li>
        <li>“The real world is never simple” — tak satu pun ukuran sepenuhnya sempurna</li>
      </ul>
```

- [ ] **Step 3: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `WACC` satisfied.

- [ ] **Step 4: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): ABC interpretation + four-measure guidance with WACC (RMK 12)"
```

---

### Task 15: Slide 21 "Riset Arus Kas" (NEW — insert before Memperbaiki SCF)

Source: `content/sections/13-research.md`. This fills the only RMK section with no slide.

**Files:**
- Modify: DECK — insert directly before `<!-- ============ SLIDE 18 — MEMPERBAIKI SCF (section) ============ -->`

- [ ] **Step 1: Insert this block**

```html
  <!-- ============ SLIDE 21 — RISET ARUS KAS ============ -->
  <section data-label="Riset Arus Kas">
    <div class="bg bg-soft">
      <div class="blob b-blue b1"></div>
      <div class="blob b-warm" style="width:380px;height:320px;left:-120px;top:160px;opacity:.45;"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="pill"></div>
    <div class="ghost br" style="bottom:-110px;">21</div>
    <div class="slide" style="flex-direction:row; gap:80px; justify-content:space-between; align-items:center;">
      <div style="max-width:660px;">
        <h2 class="display h-m anim" style="font-size:72px;">Kas &amp; akrual:<br>komplementer</h2>
        <p class="subhead sm anim d1" style="margin:34px 0 22px; color:var(--ink);">Riset arus kas — Lawson &amp; Lee</p>
        <p class="body anim d2">Lee: “Cash flow and not profit is the end result of entity activity. <strong>Profit is an abstraction</strong>; cash is a physical resource.”</p>
      </div>
      <div class="gcards anim d2">
        <div class="gcard"><span class="gn">01</span><span class="gt">Riset pasar modal: akrual informatif <strong>di atas &amp; melampaui</strong> arus kas literal</span></div>
        <div class="gcard"><span class="gn">02</span><span class="gt">Simpulan: <strong>komplementer</strong> — paling berguna bersama-sama, bukan saling menggantikan</span></div>
        <div class="gcard"><span class="gn">03</span><span class="gt">Survei FAF: bobot data arus dana <strong>naik</strong>, data akrual menurun</span></div>
      </div>
    </div>
  </section>

```

- [ ] **Step 2: Run the audit**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: FAIL overall; `Profit is an abstraction` and `Lawson` satisfied.

- [ ] **Step 3: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): new slide 21 cash-flow research — Lawson & Lee, complementarity, FAF (RMK 13)"
```

---

### Task 16: Slides 22–23 "Memperbaiki SCF" + "Sintesis" (edit old slide 18, rework old slide 19)

Source: `content/sections/14-improving-scf.md`.

**Files:**
- Modify: DECK, blocks `<!-- ============ SLIDE 18 — MEMPERBAIKI SCF (section) ============ -->` and `<!-- ============ SLIDE 19 — KONTRIBUSI ============ -->`

- [ ] **Step 1:** Memperbaiki block: comment → `SLIDE 22 — MEMPERBAIKI SCF`, pnum → `>22<`; replace its `<ul class="bul ...">` with:

```html
      <ul class="bul anim d2" style="max-width:900px;">
        <li><strong>Broome ①</strong>: wajibkan metode langsung DAN rekonsiliasi sekaligus</li>
        <li><strong>Broome ②</strong>: perbanyak panduan klasifikasi tiga seksi — persempit celah misklasifikasi</li>
        <li><strong>Broome ③</strong>: balik arah rekonsiliasi — dari arus kas operasi menuju laba bersih</li>
        <li><strong>Penulis</strong>: skedul transaksi nonkas modal kerja; skedul akuisisi tengah tahun; jelaskan sumber nonartikulasi</li>
      </ul>
```

- [ ] **Step 2:** Replace the entire Kontribusi block (through its `</section>`) with:

```html
  <!-- ============ SLIDE 23 — SINTESIS ============ -->
  <section data-label="Sintesis">
    <div class="bg bg-soft">
      <div class="blob b-warm" style="width:420px;height:340px;left:120px;top:-120px;opacity:.4;"></div>
      <div class="blob b-blue b3"></div>
    </div>
    <div class="sidepanel left" style="width:300px;">
      <div class="vtext" style="left:96px; top:50%; transform:translateY(-50%) rotate(180deg);">Sintesis</div>
    </div>
    <div class="ghost tr blue" style="font-size:300px; right:30px; top:-40px;">23</div>
    <div class="pill" style="left:calc(50% + 150px);"></div>
    <div class="slide" style="padding-left:420px; justify-content:center;">
      <h2 class="subhead anim" style="font-size:46px; color:var(--ink); margin-bottom:60px;">Sintesis penutup</h2>
      <div class="statgrid anim d1" style="gap:50px 90px; max-width:1020px;">
        <div class="stat"><div class="sq"></div><div class="col"><span class="num" style="font-size:24px; font-weight:800;">Kasus khusus SCFP</span><span class="txt">Dana didefinisikan sebagai kas; laporan derivatif yang tetap melahirkan informasi baru</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num" style="font-size:24px; font-weight:800;">Pilihan proprietary</span><span class="txt">Bunga &amp; dividen di seksi operasi — sumber isu klasifikasi; IAS 7 fleksibel asal konsisten</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num" style="font-size:24px; font-weight:800;">Dua masalah menetap</span><span class="txt">Nonartikulasi dan misklasifikasi — dibaca utuh, SCF tetap memperingatkan (WorldCom)</span></div></div>
        <div class="stat"><div class="sq"></div><div class="col"><span class="num" style="font-size:24px; font-weight:800;">Penilaian afirmatif</span><span class="txt">Konsistensi, daya prediksi, komparabilitas naik — SCF kian penting karena bebas <em>arbitrariness</em> laba</span></div></div>
      </div>
      <p class="body anim d3" style="margin-top:52px; font-size:20px; color:var(--ink-faint);">Sumber: Wolk, Dodd &amp; Rozycki (2017), <em>Accounting Theory</em>, 9th ed., Bab 13</p>
    </div>
  </section>
```

- [ ] **Step 3: Run the audit — expect FULL PASS**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: `AUDIT: PASS — 23 slides, all gates green`

- [ ] **Step 4: Commit**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "feat(ppt-k2): Broome recommendations explicit + sintesis close (RMK 14) — audit green"
```

---

### Task 17: Final verification (render + coverage)

**Files:**
- Read-only: DECK, spec, RMK sections

- [ ] **Step 1: Audit gate**

Run: `python "PPT Kelompok 2 PKK/tools/audit_deck.py"`
Expected: `AUDIT: PASS — 23 slides, all gates green`

- [ ] **Step 2: Coverage audit against the spec table.** For each of the 23 rows in the spec's "Target structure" table, confirm the slide exists with the specified content. Read the deck top to bottom once, checking each slide against its spec row. Any mismatch → fix and re-run Step 1.

- [ ] **Step 3: Render check.** Open the deck in a browser (`start "" "PPT Kelompok 2 PKK\Statement of Cash Flows.html"` from PowerShell, or use any available browser tool). Navigate all 23 slides with →. Confirm: no console errors; no text overflowing slide bounds (watch slide 6's 3×2 statgrid, slide 8's taller table, slide 12's 4 cards); ghost numbers don't collide with tables. If a browser tool is unavailable, state that visual verification was not performed — do not claim it passed.

- [ ] **Step 4: Number spot-audit.** Grep the deck for `\$[\d,.]+` and tie every distinct figure to its RMK source line (sections 01, 05, 06, 07, 09, 10, 12 contain all on-slide numbers). Zero unmatched figures allowed.

- [ ] **Step 5: Final commit (if Steps 2–4 produced fixes)**

```bash
git add "PPT Kelompok 2 PKK/Statement of Cash Flows.html"
git commit -m "chore(ppt-k2): final verification fixes — RMK-aligned 23-slide deck complete"
```
