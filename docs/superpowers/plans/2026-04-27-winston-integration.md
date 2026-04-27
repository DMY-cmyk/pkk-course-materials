# Winston MIT Framework Integration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Mengeksekusi spec `docs/superpowers/specs/2026-04-27-winston-integration-design.md` untuk menghasilkan 9 artefak: 1 referensi framework (`.claude/winston-framework.md`), 2 spec deck-level, 1 template rubrik slide-level, 4 dokumen audit deck v5, dan 1 file duplikat `v6-winston.html`.

**Architecture:** Eksekusi dalam tiga gelombang sesuai aliran data spec. Gelombang 1 (Codification, T1–T5): membangun lapisan tata kelola — single source of truth → spec turunan → template rubrik. Gelombang 2 (Duplication, T2): satu perintah `cp` + verifikasi `md5sum`. Gelombang 3 (Audit, T6–T9): membaca `Pelaporan Keuangan Korporat Gr3 v5 (1).html`, membangun inventori slide × crime dengan bukti konkret, lalu menyintesis prioritas dan naratif audit. Tidak ada modifikasi konten v6 dalam plan ini — itu pekerjaan executing-plans selanjutnya.

**Tech Stack:** Markdown (semua artefak), HTML reading via Read/Grep tools, `cp` + `md5sum` (Bash), `git` untuk commit per task. Tidak ada kode runtime; verifikasi = checklist acceptance criteria spec V1–V7.

**Bahasa Konten:** Artefak ditulis dalam Bahasa Indonesia formal akademik (sesuai spec) kecuali transkripsi langsung dari jpeg Winston (Bahasa Inggris) di `winston-framework.md`. Filename, label kode, dan perintah shell tetap English.

**Aturan Tegas (dari spec, jangan dilanggar):**
- E1 Klausul Supremasi FASB — substansi FASB selalu menang atas Winston.
- E2 Pisahkan design vs delivery crimes — hanya design crimes masuk crime-inventory.
- E3 Angka adalah prop di slide kasus INDF.
- E4 Defect HIGH-XL diangkat ke spec, bukan patch.
- E5 STAR ditulis dwibahasa.
- Sumber `sources/group-work-original/` selamanya read-only.
- File `Pelaporan Keuangan Korporat Gr3 v5 (1).html` adalah control sample — tidak disentuh.

---

## File Structure

| # | Path | Tanggung Jawab | Dependensi |
|---|------|----------------|------------|
| 1 | `.claude/winston-framework.md` | Single source of truth — transkripsi 5 framework + tabel referensi silang fase | (none) |
| 2 | `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html` | Duplikat byte-identik v5; placeholder revisi | v5 file |
| 3 | `specs/presentation-design-spec.md` | Deck-level: Empowerment Promise, STAR, Vision, Contributions Close, struktur 32 slide | T1 |
| 4 | `specs/winston-integration-rules.md` | Klausul Supremasi FASB + aturan resolusi E2–E5 + pemetaan framework × fase | T1 |
| 5 | `rubrics/_template.md` | Template rubrik slide universal — 10 design crimes + slot STAR + trigger F5 | T1 |
| 6 | `analysis/winston-audit/crime-inventory.md` | Tabel slide × crime × bukti × severity × effort untuk 32 slide v5 | T1 |
| 7 | `analysis/winston-audit/revision-priorities.md` | Tier HIGH/MEDIUM/LOW + flag HIGH-XL | T6 |
| 8 | `analysis/winston-audit/audit-deck-v5.md` | Naratif per framework + area v5 yang sudah selaras | T6 |
| 9 | `analysis/winston-audit/delivery-checklist.md` | Crimes presenter (bukan file) | T1 |

---

## Task 1: Bangun `.claude/winston-framework.md` (Single Source of Truth)

**Files:**
- Create: `.claude/winston-framework.md`
- Read: `Patrcik Winston MIT Presentation Master/1. Start Any Presentation Right.jpeg`
- Read: `Patrcik Winston MIT Presentation Master/2. Slides Crimes.jpeg`
- Read: `Patrcik Winston MIT Presentation Master/3. Unforgetable Idea.jpeg`
- Read: `Patrcik Winston MIT Presentation Master/4. Persuade Talk Structure.jpeg`
- Read: `Patrcik Winston MIT Presentation Master/5. Props & Stories.jpeg`

- [ ] **Step 1: Baca lima jpeg Winston**

Gunakan tool Read pada setiap jpeg untuk mengekstrak Role/Task/Steps/Rules/Output secara persis. Jangan parafrase; transkripsi literal.

- [ ] **Step 2: Tulis dokumen dengan struktur berikut**

```markdown
# Patrick Winston MIT Presentation Master — Reference

> Single source of truth for the 5 frameworks distilled from Winston's
> "How To Speak" MIT lecture. All other Winston-derived artefacts in this
> repo (specs, rubrics, audits) MUST cite this file. To revise Winston
> guidance, edit this file first then propagate downward.

**Source:** `Patrcik Winston MIT Presentation Master/*.jpeg` (5 infographic cards from getintoai Instagram, distilling Winston's MIT lecture).

**Layer mapping:**

| Framework | Layer | Governs |
|-----------|-------|---------|
| F1 Start Right | DECK-LEVEL | `specs/presentation-design-spec.md` (opening slide & first 60s) |
| F2 Slide Crimes | SLIDE-LEVEL | `rubrics/_template.md` (per-slide checklist) |
| F3 STAR (Unforgettable) | DECK-LEVEL | `specs/presentation-design-spec.md` (deck core idea) |
| F4 Persuade Structure | DECK-LEVEL | `specs/presentation-design-spec.md` (32-slide architecture) |
| F5 Props & Stories | SLIDE-LEVEL | `rubrics/_template.md` (trigger for INDF case + difficult concept slides) |

**Phase mapping (CLAUDE.md):**

| Framework | Phase 1 (brainstorm) | Phase 3 (plan) | Phase 4 (build) | Phase 4 (review) |
|-----------|----------------------|----------------|-----------------|-------------------|
| F1 | input | required output | applied to slide 1 | gate |
| F2 | (n/a) | rubric items | applied per slide | gate |
| F3 | input | required output | applied throughout | gate |
| F4 | input | required output | block boundaries | gate |
| F5 | input | required output | case+concept slides | gate |

---

## F1 — START ANY PRESENTATION RIGHT [DECK-LEVEL]

**Prompt role:** Act as a presentation coach applying Patrick Winston's
MIT framework — every talk must open with an empowerment promise that
tells the audience exactly what they will know by the end that they
didn't know at the beginning.

**Task:** Write a powerful opening that makes the audience immediately
understand why staying is worth every minute of their time.

**Steps:**
1. Ask for presentation topic, audience, and desired outcome before starting
2. Identify the single most valuable thing the audience will walk away knowing
3. Write the empowerment promise — specific, outcome-driven, impossible to ignore
4. Design the first 60 seconds — promise, context, and why this matters now
5. Flag everything that should be cut from the opening — jokes, thank yous, apologies

**Rules:**
- Never open with a joke — audience isn't ready
- Never open with "thank you for having me" — weak and forgettable
- Empowerment promise must be specific — not "you'll learn about X" but "by the end you'll be able to do Y"
- First 60 seconds must earn the next 60 minutes
- Cut everything that doesn't serve the promise

**Output chain:** Empowerment Promise → First 60 Seconds → What to Cut → Opening Script

---

## F2 — ELIMINATE YOUR SLIDE CRIMES [SLIDE-LEVEL]

**Prompt role:** Act as a slide crime investigator applying Patrick
Winston's MIT framework — every presentation crime that puts audiences
to sleep gets identified, prosecuted, and eliminated.

**Task:** Audit slides and eliminate every crime Winston identified that
makes audiences disengage, sleep, or leave mentally.

**The 10 Slide Crimes:**
1. Too many slides
2. Too many words per slide
3. Font size under 40pt
4. Reading slides aloud *(DELIVERY CRIME — not auditable from file)*
5. Laser pointer usage *(DELIVERY CRIME)*
6. Speaker standing far from slides *(DELIVERY CRIME)*
7. No white space or air
8. Background clutter and logos
9. Collaborators list as final slide
10. "Thank you" or "Questions?" as final slide

**Steps:**
1. Ask to describe or share current slides before starting
2. Check for the 10 Winston slide crimes
3. Flag every crime with a specific fix
4. Redesign the final slide as a contributions slide
5. Deliver a clean slide brief — what stays, what goes, what changes

**Rules:**
- Every crime must have a specific fix — not just a flag
- Font minimum 40pt — no exceptions
- Final slide must be contributions — never questions or thank you
- White space is not wasted space — it's breathing room for the audience's brain
- Slides are condiments — not the main event

**Output chain:** Crime Audit → Fix per Crime → Final Slide Redesign → Clean Slide Brief

**Audit separation per spec E2:** Crimes #4, #5, #6 are delivery crimes (only auditable during live presentation). They go to `delivery-checklist.md`, not `crime-inventory.md`.

---

## F3 — MAKE YOUR IDEAS UNFORGETTABLE (STAR) [DECK-LEVEL]

**Prompt role:** Act as a personal brand architect applying Winston's Star
framework — Symbol, Slogan, Surprise, Salient idea, Story — to make any
idea impossible to forget.

**Task:** Apply Winston's Star to the core idea so it sticks in every
audience's mind long after the presentation ends.

**Steps:**
1. Ask for core idea, audience, and what to remember
2. Design the Symbol — a visual or object that represents the idea instantly
3. Write the Slogan — a short phrase that becomes the handle people use
4. Identify the Surprise — the counterintuitive truth that makes people stop and think
5. Sharpen the Salient idea — the one idea that sticks above everything else
6. Build the Story — how it works, why it matters, the journey that led here

**Rules:**
- Symbol must be visual and specific — not abstract
- Slogan must be repeatable in a meeting without explanation
- Surprise must genuinely challenge an assumption — not just be interesting
- Salient idea must be one — never two or three
- Story must be personal enough to be specific, universal enough to resonate

**Output chain:** Symbol → Slogan → Surprise → Salient Idea → Story → Winston Star Summary

**Indonesian adaptation per spec E5:** Slogan diuji dalam Bahasa Indonesia. Bagian English disertakan di catatan kaki untuk traceability.

---

## F4 — STRUCTURE ANY TALK THAT PERSUADES [DECK-LEVEL]

**Prompt role:** Act as a persuasion architect applying Winston's job talk
framework — vision, proof of work, and contributions — to any presentation
that needs to convince, convert, or close.

**Task:** Structure the talk so the audience knows the vision, believes
something significant has been done, and remembers exactly what was
contributed — all within the first 5 minutes.

**Steps:**
1. Ask for goal, audience, and desired post-talk action
2. Build the vision statement — the problem someone cares about and the new approach
3. Design the proof of work — the steps taken that prove something real
4. Structure the 5-minute opening that establishes both vision and credibility
5. Build the contributions close — the final slide that mirrors the opening promise

**Rules:**
- Vision must be established within 5 minutes — never later
- Proof of work must be specific steps — not vague accomplishments
- Opening and close must mirror each other — promise made, promise kept
- Contributions slide stays up during questions — never replaced with "thank you"
- Every minute must advance either vision or proof — nothing else

**Output chain:** Vision Statement → Proof of Work → 5-Minute Opening → Contributions Close → Full Talk Structure

---

## F5 — USE PROPS AND STORIES TO TEACH ANYTHING [SLIDE-LEVEL]

**Prompt role:** Act as a teaching design specialist applying Winston's
prop and storytelling frameworks — the techniques that make ideas feel
physical, memorable, and impossible to misunderstand.

**Task:** Design a prop or story that makes the most complex idea feel as
simple and physical as holding it in your hands.

**Steps:**
1. Ask for the complex idea to teach and audience
2. Identify the single most confusing aspect of the idea
3. Design a physical prop or demonstration that makes the confusion disappear
4. Build a story around the prop — tension, demonstration, resolution
5. Write the verbal script that guides the audience from confusion to clarity

**Rules:**
- Prop must be physical and demonstrable — not a slide or diagram
- Story must have genuine tension before resolution
- Script must guide attention — tell them where to look and what to notice
- Demonstration must work even if it fails — the failure itself teaches
- If no physical prop exists, design the closest verbal equivalent

**Output chain:** Confusing Concept → Prop Design → Story Arc → Verbal Script → Teaching Sequence

**Adaptation for INDF case slides per spec E3:** Numbers are the prop. Required story arc: konteks/ketegangan → demonstrasi (tabel/grafik) → resolusi (interpretasi via FASB).
```

- [ ] **Step 3: Verifikasi acceptance V1 dari spec**

Periksa:
- Kelima framework punya Role/Task/Steps/Rules/Output lengkap.
- Setiap framework berlabel `[DECK-LEVEL]` atau `[SLIDE-LEVEL]`.
- Tabel layer mapping dan phase mapping ada.
- Tidak ada `TODO`, `TBD`, atau placeholder.

- [ ] **Step 4: Commit**

```bash
git add .claude/winston-framework.md
git commit -m "docs(winston): add framework reference (single source of truth)

Transcribes the 5 Winston frameworks from Patrcik Winston MIT
Presentation Master/*.jpeg into a single canonical reference. Labels
each framework as DECK-LEVEL or SLIDE-LEVEL and maps them to phases
in CLAUDE.md. All other Winston-derived artefacts cite this file.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: Duplikasi v5 → v6-winston.html (Aliran C)

**Files:**
- Read: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html`
- Create: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html`

- [ ] **Step 1: Salin file dengan `cp`**

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/Pelaporan Keuangan Korporat Gr. 3"
cp "Pelaporan Keuangan Korporat Gr3 v5 (1).html" "Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```

- [ ] **Step 2: Verifikasi byte-identik via md5sum**

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat/Pelaporan Keuangan Korporat Gr. 3"
md5sum "Pelaporan Keuangan Korporat Gr3 v5 (1).html" "Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```

Expected: kedua hash MD5 **identik**. Jika berbeda, salin ulang.

- [ ] **Step 3: Commit**

```bash
git add "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
git commit -m "feat(deck): duplicate v5 to v6-winston.html as audit target

Byte-identical copy of v5 (1).html for the Winston revision pass.
Per spec V6: no content modification yet — placeholder only.
Original v5 remains untouched as control sample.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: Bangun `specs/presentation-design-spec.md` (Deck-Level)

**Files:**
- Create: `specs/presentation-design-spec.md`
- Read: `.claude/winston-framework.md` (untuk referensi F1, F3, F4)
- Read: `sources/fasb-conceptual-framework.pdf` (untuk Salient Idea)
- Read: `sources/indf-2024-ar.pdf` (untuk Story material)

- [ ] **Step 1: Tulis dokumen dengan skeleton berikut**

```markdown
# Group 3 PKK — Presentation Design Spec (Deck-Level)

**Source:** Diturunkan dari `.claude/winston-framework.md` (F1, F3, F4).
**Cakupan:** Tata kelola arsitektur deck (sekali per deck), bukan rubrik
slide individual. Untuk slide-level, lihat `rubrics/_template.md`.

---

## 1. Empowerment Promise (F1)

> *"Di akhir presentasi 30 menit ini, Anda akan mampu [Y yang spesifik
> dan dapat diuji]."*

**Promise final (Bahasa Indonesia, akan diucapkan di kelas):**

[TULIS SATU KALIMAT SPESIFIK. Contoh placeholder yang HARUS diganti:
"...Anda akan mampu mengidentifikasi tiga keputusan akuntansi konkret
INDF 2024 yang gagal memenuhi standar Faithful Representation FASB."]

**English fallback (per E5):**

[Tulis ekuivalen English untuk traceability ke Winston asli.]

**60-Second Opening Script (slide 1–3):**

[Tulis script verbal 3 paragraf — promise, konteks, mengapa penting
sekarang. Total ≈150 kata = 60 detik bicara.]

**What to Cut (eksplisit, per F1 rules):**
- Tidak ada lelucon pembuka
- Tidak ada "Terima kasih sudah hadir"
- Tidak ada permintaan maaf ("maaf masih belajar", dll)

---

## 2. STAR Core Idea (F3)

### Symbol

**Symbol (visual ikonik untuk seluruh deck):**

[Deskripsi visual — mis. "Rumah dengan fondasi → tiang → atap, di mana
fondasi = Conceptual Framework, tiang = qualitative characteristics,
atap = financial statements". Wajib dapat digambar dalam 5 detik.]

### Slogan

**Slogan Bahasa Indonesia (akan diulang min. 3 kali di deck):**

[Frasa pendek, ≤7 kata. Contoh: "Conceptual Framework adalah konstitusi
laporan keuangan."]

**English (catatan kaki untuk traceability):**

[Translation.]

### Surprise

**Surprise (kebenaran kontra-intuitif):**

[Satu klaim yang menentang asumsi awam. Contoh: "Conceptual Framework
bukan aturan akuntansi — ia justru di atas semua aturan dan
mengalahkan PSAK ketika PSAK ambigu."]

### Salient Idea

**Salient Idea (satu, bukan dua/tiga, per F3 rules):**

[Satu kalimat. WAJIB tidak melanggar E1: jika satu kalimat tidak cukup
untuk substansi FASB, tetap pilih satu kalimat untuk *deck-level*; biarkan
slide individual mengangkut komponennya.]

### Story

**Story (personal namun universal):**

[Naratif 3–4 kalimat. Konteks → ketegangan → resolusi. INDF 2024 sebagai
kasus konkret. Dapat berupa anekdot dari AR INDF — mis. tantangan
recognition timing pada penurunan margin.]

---

## 3. Vision Statement & Persuade Structure (F4)

### Vision Statement (≤5 menit pertama deck)

**Problem:** [Masalah yang dipedulikan audiens kelas S2 PKK.]

**New approach:** [Pendekatan yang ditawarkan presentasi ini.]

### Proof of Work (slide 4–29)

**Bukti spesifik bahwa presentasi ini sudah melakukan pekerjaan riil:**

- [Sebutan ke pembacaan FASB CF 2024 yang utuh]
- [Sebutan ke audit angka INDF 2024 AR yang spesifik]
- [Sebutan ke triangulasi dengan Wolk/Scott textbook]

### Contributions Close (slide 30–32, F4 + F2 crime #10)

**Slide penutup TIDAK boleh "Terima Kasih" atau "Pertanyaan?"** (Crime #10).

Slide 30–32 berisi **kontribusi konkret kelompok**:

- Slide 30: [Kontribusi 1 — mis. "Tiga area di mana INDF 2024 melebihi
  ekspektasi Faithful Representation"]
- Slide 31: [Kontribusi 2]
- Slide 32: [Kontribusi 3 / Q&A — slide kontribusi tetap di layar saat
  Q&A, per F4 rules]

---

## 4. Struktur 32 Slide

| Blok | Slide # | Fungsi | Framework Wajib |
|------|---------|--------|-----------------|
| Opening | 1–3 | Cover + Empowerment Promise + Vision | F1, F3 (Symbol intro) |
| Proof of Work | 4–29 | FASB CF konten + INDF case + analisis | F2 (semua), F3 (Slogan recurring), F5 (slide kasus) |
| Contributions Close | 30–32 | Kontribusi + Q&A staging | F4 (mirror opening) |

---

## 5. Verifikasi (V2)

- [ ] Empowerment Promise satu kalimat Bahasa Indonesia ✓
- [ ] STAR lengkap S–T–A–R dwibahasa ✓
- [ ] Vision Statement + Contributions Close ada ✓
- [ ] Pembagian 32 slide ke opening (1–3) / proof (4–29) / close (30–32) ✓
- [ ] Tidak ada placeholder yang belum diisi ✓
```

- [ ] **Step 2: Isi semua placeholder `[...]` dengan konten substantif**

Setiap `[...]` harus diganti dengan konten riil berbasis FASB CF + INDF AR. Tidak boleh ada `[...]` tersisa di file final.

- [ ] **Step 3: Verifikasi V2 acceptance**

```bash
grep -n '\[' "specs/presentation-design-spec.md" | grep -v '^[0-9]*:.*\[ \]'
```

Expected: tidak ada output (semua `[...]` placeholder sudah diisi; hanya checklist `[ ]` yang boleh tersisa).

- [ ] **Step 4: Commit**

```bash
git add specs/presentation-design-spec.md
git commit -m "docs(spec): add deck-level presentation design (F1, F3, F4)

Defines Empowerment Promise, STAR core idea (Symbol, Slogan, Surprise,
Salient, Story), Vision Statement, and Contributions Close for the
32-slide Group 3 deck. Per E1 FASB Supremacy: STAR Salient is
deck-level summary; FASB substance lives at slide level intact.
Per E5: dwibahasa Indonesia primary, English footnote.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: Bangun `specs/winston-integration-rules.md` (Proses & Aturan)

**Files:**
- Create: `specs/winston-integration-rules.md`
- Read: `.claude/winston-framework.md`
- Read: `docs/superpowers/specs/2026-04-27-winston-integration-design.md` (untuk teks E1–E5)

- [ ] **Step 1: Tulis dokumen dengan skeleton berikut**

```markdown
# Winston Integration — Process & Resolution Rules

**Source:** Spec `docs/superpowers/specs/2026-04-27-winston-integration-design.md` Bagian 5.
**Tujuan:** Aturan tetap untuk menyelesaikan konflik antara Winston dan
substansi/konteks akademik PKK.

---

## E1 — Klausul Supremasi FASB (TEGAS)

**Aturan:** Substansi FASB Conceptual Framework + Week 5 selalu menang
atas Winston. Winston adalah *lensa retorika*, bukan editor konten
akademik.

**Operasionalisasi:**
- Bila satu framework Winston memaksa pemotongan substansi FASB, framework
  itu **diadaptasi** — bukan substansi FASB yang dipotong.
- Contoh: Winston "satu salient idea" vs FASB "Relevance + Faithful
  Representation". Resolusi: salient idea hidup di level *deck*; Relevance
  dan Faithful Representation tetap muncul utuh di slide masing-masing.
- Reviewer Phase 4 wajib menolak fix Winston yang melanggar klausul ini.

---

## E2 — Pemisahan Design Crimes vs Delivery Crimes

**Aturan:** Crimes Winston #4 (reading aloud), #5 (laser pointer), #6
(speaker distance) adalah *delivery crimes* — hanya dapat dinilai saat
presentasi langsung, bukan dari file.

**Operasionalisasi:**
- `analysis/winston-audit/crime-inventory.md` hanya memuat design crimes
  (#1, #2, #3, #7, #8, #9, #10).
- Delivery crimes pindah ke `analysis/winston-audit/delivery-checklist.md`
  sebagai catatan presenter.

---

## E3 — Slide Kasus INDF: Angka sebagai Prop

**Aturan:** Untuk slide kasus, **angka adalah prop**. Penyajian wajib
mengikuti story arc F5: konteks/ketegangan → demonstrasi (tabel/grafik)
→ resolusi (interpretasi via FASB).

**Operasionalisasi:**
- Tabel polos tanpa story arc = crime tambahan khusus slide kasus.
- Rubrik slide kasus (`rubrics/_template.md`) wajib memicu F5 secara
  otomatis.

---

## E4 — Defect HIGH-XL: Diangkat ke Spec, Bukan Patch v6

**Aturan:** Bila audit menemukan defect HIGH severity dengan effort XL
(mis. font 24pt di seluruh deck), perbaikan tidak terjadi sebagai patch
di `v6-winston.html` melainkan menjadi *requirement* untuk Phase 4 build
dari nol.

**Operasionalisasi:**
- `analysis/winston-audit/revision-priorities.md` wajib menandai entri
  HIGH-XL dengan flag "needs full redesign, not patch".
- Eksekutor Phase 4 wajib membaca flag ini sebelum mulai build.

---

## E5 — Dwibahasa: Indonesia Primer, Inggris Catatan Kaki

**Aturan:** Sintesis STAR ditulis dwibahasa di
`presentation-design-spec.md`. Slogan diuji dalam Bahasa Indonesia (yang
akan diucapkan di kelas), dengan terjemahan Inggris di catatan kaki untuk
traceability ke Winston asli.

**Operasionalisasi:**
- Semua artefak Winston-derived: Bahasa Indonesia primer, English
  diizinkan untuk istilah teknis dan transkripsi langsung dari sumber
  Winston.

---

## Pemetaan Framework × Fase CLAUDE.md

| Framework | Phase 1 | Phase 3 | Phase 4 build | Phase 4 review |
|-----------|---------|---------|---------------|-----------------|
| F1 Start Right | Input brainstorm: bentuk Empowerment Promise | Output wajib di `presentation-design-spec.md` | Diaplikasikan ke slide 1–3 | Reviewer cek slide 1 berisi promise |
| F2 Slide Crimes | (n/a) | Item rubrik tiap slide | Diaplikasikan per slide saat build | Reviewer cek 7 design crimes |
| F3 STAR | Input brainstorm: cari Symbol/Slogan | Output wajib di `presentation-design-spec.md` | Symbol muncul di ≥3 slide; Slogan ≥3× | Reviewer cek STAR alignment |
| F4 Persuade | Input brainstorm: tetapkan blok 3-segment | Output wajib (struktur 32 slide) | Boundaries slide 3/4 dan 29/30 | Reviewer cek slide 32 = contributions |
| F5 Props & Stories | Input brainstorm: tandai slide kasus | Output rubrik trigger | Aplikasi pada slide kasus + konsep sulit | Reviewer cek story arc |

---

## Verifikasi (V3)

- [ ] Klausul Supremasi FASB tegas dan eksplisit ✓
- [ ] Aturan E2–E5 lengkap ✓
- [ ] Pemetaan framework × fase CLAUDE.md lengkap ✓
```

- [ ] **Step 2: Verifikasi V3 acceptance**

Baca file dan pastikan:
- E1 muncul sebagai bagian terpisah dengan kata "TEGAS" / "supremacy".
- E2, E3, E4, E5 masing-masing punya bagian terpisah.
- Tabel pemetaan framework × fase ada lengkap untuk F1–F5 × Phase 1, 3, 4 build, 4 review.

- [ ] **Step 3: Commit**

```bash
git add specs/winston-integration-rules.md
git commit -m "docs(spec): add Winston integration process rules (E1-E5)

Codifies the FASB Supremacy Clause (E1), design vs delivery crime
separation (E2), numbers-as-prop rule for INDF case slides (E3),
HIGH-XL escalation to redesign (E4), and dwibahasa output convention
(E5). Maps each Winston framework to its required role in CLAUDE.md
phases 1, 3, and 4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: Bangun `rubrics/_template.md` (Slide-Level Universal Template)

**Files:**
- Create: `rubrics/_template.md`
- Read: `.claude/winston-framework.md` (untuk F2, F5)
- Read: `.claude/CLAUDE.md` (untuk front-matter slide convention)

- [ ] **Step 1: Tulis template dengan skeleton berikut**

````markdown
<!--
slide: NN
role: [cover|agenda|section-divider|content|case|chart|table|quote|synthesis|qanda]
title: "..."
learning_objective: "..."
sources:
  - doc: fasb-conceptual-framework
    ref: "Chapter X, QCY–QCZ"
assigned_to: "member-name"
rubric: rubrics/slide-NN.md
last_reviewed: YYYY-MM-DD
-->

# Rubric — Slide NN: [Judul]

> Template universal. Setiap rubrik slide individual (`slide-01.md` …
> `slide-32.md`) menyalin struktur ini dan mengisi setiap section.

## 1. Front-Matter Compliance

- [ ] Front-matter HTML comment lengkap sesuai CLAUDE.md `# File Conventions`
- [ ] `role` dipilih dari enum yang valid
- [ ] `learning_objective` satu kalimat, dapat diuji
- [ ] `sources` mengutip FASB CF / INDF AR / Week 5 / Wolk / Scott — tidak fabrikasi

## 2. F2 Design Crimes Checklist (per E2 — delivery crimes excluded)

- [ ] **Crime #1 — Too many slides:** Slide ini perlu? Jika substansi
      sudah ada di slide tetangga, gabung.
- [ ] **Crime #2 — Too many words:** ≤25 kata di body slide. Catatan
      presenter menampung kata berlebih.
- [ ] **Crime #3 — Font ≥40pt:** Tidak ada teks <40pt yang dapat dibaca
      audiens. Footnote diizinkan ≥24pt.
- [ ] **Crime #7 — White space sufficient:** Minimal 30% area slide
      kosong. White space adalah breathing room, bukan ruang sia-sia.
- [ ] **Crime #8 — No background clutter:** Tidak ada watermark, logo
      ganda, gradient mengganggu. Logo institusi hanya di slide 1 & 32.
- [ ] **Crime #9 — Not collaborators-list-as-final:** Jika ini slide
      penutup deck, BUKAN daftar nama anggota.
- [ ] **Crime #10 — Not "Thank you" / "Questions?":** Jika ini slide
      penutup deck, BUKAN "Terima Kasih" atau "Pertanyaan?". Wajib
      kontribusi.

> Crimes #4 (reading aloud), #5 (laser pointer), #6 (speaker distance)
> dipindah ke `analysis/winston-audit/delivery-checklist.md` per E2.

## 3. F5 Trigger — Props & Stories

- [ ] **Apakah slide ini termasuk:**
  - Slide kasus INDF (mengandung angka AR)?
  - Slide konsep sulit (mis. going concern, faithful representation,
    materiality)?
- [ ] **Jika YA, slide WAJIB mengikuti story arc F5:**
  - [ ] Konteks/ketegangan teridentifikasi (apa yang membuat audiens
        bingung sebelum slide ini?)
  - [ ] Demonstrasi konkret (angka spesifik / contoh / diagram)
  - [ ] Resolusi (interpretasi via FASB)
- [ ] **Per E3:** Untuk slide kasus, angka adalah prop. Tabel polos
      tanpa narasi = pelanggaran.

## 4. STAR Alignment (deck-level F3 cek)

Slide ini menguatkan elemen STAR mana?

- [ ] **Symbol:** Slide ini menampilkan/merujuk Symbol deck? (slide
      Symbol-bearing wajib min. 3 dalam deck)
- [ ] **Slogan:** Slogan deck muncul di slide ini? (target ≥3× per deck)
- [ ] **Surprise:** Slide ini membongkar kebenaran kontra-intuitif?
- [ ] **Salient idea:** Slide ini berkontribusi ke salient idea, bukan
      tangent?
- [ ] **Story:** Slide ini adalah node di story arc deck?

## 5. FASB Supremacy Verifikasi (E1)

- [ ] Substansi FASB di slide ini tidak dikorbankan demi gaya Winston.
- [ ] Bila ada konflik (mis. F2 #2 ≤25 kata vs definisi FASB lengkap),
      definisi FASB tetap utuh — pertimbangkan split ke 2 slide.

## 6. Sumber & Traceability

- [ ] Setiap klaim numerik mengutip halaman/lokasi di INDF AR atau FASB CF.
- [ ] Tidak ada angka fabrikasi (per CLAUDE.md aturan #3).

## 7. Tanda Tangan Reviewer

- Reviewer 1 (peer): __________ tanggal __________
- Reviewer 2 (final): __________ tanggal __________
````

- [ ] **Step 2: Verifikasi V4 acceptance**

Periksa file:
- Front-matter HTML comment ada di awal sesuai CLAUDE.md.
- Section "F2 Design Crimes Checklist" memuat hanya 7 crime (1, 2, 3, 7, 8, 9, 10) — bukan 10.
- Catatan eksplisit bahwa #4, #5, #6 dipindah ke delivery checklist.
- Section "F5 Trigger" memuat kondisi slide kasus + slide konsep sulit.
- Section "STAR Alignment" memuat 5 sub-checklist (S, T, A, R, dan Story).

- [ ] **Step 3: Commit**

```bash
git add rubrics/_template.md
git commit -m "docs(rubric): add universal slide rubric template (F2 + F5 + STAR)

Provides the per-slide checklist that every rubrics/slide-NN.md will
inherit. Includes 7 design crimes (per E2 — delivery crimes excluded),
F5 trigger for INDF case + difficult-concept slides, STAR alignment
slot, and FASB Supremacy verification (E1).

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: Audit v5 → `analysis/winston-audit/crime-inventory.md`

**Ini task terberat. Bagi menjadi sub-langkah agar dapat dilakukan dalam batch.**

**Files:**
- Create: `analysis/winston-audit/crime-inventory.md`
- Read: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html`
- Read: `Pelaporan Keuangan Korporat Gr. 3/screenshots/` (jika ada thumbnail per slide)
- Read: `.claude/winston-framework.md` (rules F2)

- [ ] **Step 1: Bangun slide inventory dari v5.html**

Baca file `v5 (1).html` sepenuhnya. Identifikasi setiap slide (cari pola `<section`, `class="slide"`, atau marker yang dipakai deck). Catat untuk setiap slide:
- Nomor slide
- Judul (jika ada)
- Jumlah kata di body
- Estimasi font size (cari CSS `font-size`)
- Apakah ada white space cukup (estimasi visual)
- Apakah ada clutter/logo yang menonjol
- Slot khusus: slide pertama (cek F1), slide terakhir (cek F2 #9, #10)

- [ ] **Step 2: Tulis crime-inventory.md dengan skeleton berikut**

```markdown
# Winston Slide Crime Inventory — Deck v5 (1)

**Source file:** `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html`
**Audit date:** YYYY-MM-DD
**Framework reference:** `.claude/winston-framework.md` F2 (10 Slide Crimes)
**Scope:** Hanya design crimes (#1, #2, #3, #7, #8, #9, #10) per E2.
Delivery crimes di `delivery-checklist.md`.

---

## Executive Summary (Aggregate)

| Severity | Count |
|----------|-------|
| HIGH | NN |
| MEDIUM | NN |
| LOW | NN |
| **Total** | NN |

| Effort | Count |
|--------|-------|
| S | NN |
| M | NN |
| L | NN |
| XL | NN |

| Crime | Total Occurrences |
|-------|-------------------|
| #1 Too many slides | NN |
| #2 Too many words | NN |
| #3 Font <40pt | NN |
| #7 No white space | NN |
| #8 Background clutter | NN |
| #9 Collaborators as final slide | NN |
| #10 "Thank you" / "Questions?" final | NN |

**HIGH-XL flagged entries (per E4):** NN
> Defect HIGH-XL diangkat ke Phase 4 redesign — bukan patch v6.

---

## Per-Slide Inventory

| Slide # | Crime # | Bukti (Quote/Loc) | Severity | Effort | Fix Diusulkan |
|---------|---------|--------------------|----------|--------|----------------|
| 01 | (none) | — | — | — | — |
| 02 | #2 | "Lorem ipsum 47 words..." (line 142) | MED | S | Potong ke ≤25 kata, sisanya ke notes |
| ... | ... | ... | ... | ... | ... |
| 32 | #10 | `<h1>Terima Kasih</h1>` (line 1840) | HIGH | M | Ganti ke contributions slide |
```

- [ ] **Step 3: Isi tabel per-slide untuk SEMUA 32 slide**

Setiap baris wajib:
- **Slide #:** 01 sampai 32
- **Crime #:** Salah satu dari 7 design crimes; jika tidak ada crime, tulis `(none)` dan kosongkan kolom lain.
- **Bukti:** Kutipan teks atau lokasi line number di v5.html. Tidak boleh asumsi tanpa bukti.
- **Severity:** HIGH (mengganggu pemahaman / merusak kredibilitas), MED (mengurangi efektivitas), LOW (kosmetik).
- **Effort:** S (≤15 menit edit), M (15–60 menit), L (1–4 jam restruktur), XL (>4 jam, butuh redesain).
- **Fix:** Spesifik. Tidak boleh "perbaiki saja" — sebut tindakan konkret.

Bila satu slide melanggar beberapa crime, buat baris terpisah per crime.

- [ ] **Step 4: Hitung agregat dan isi Executive Summary**

Setelah tabel selesai, hitung:
- Jumlah HIGH/MED/LOW
- Jumlah S/M/L/XL
- Jumlah per crime
- Jumlah HIGH-XL (flag E4)

Isi Executive Summary di bagian atas.

- [ ] **Step 5: Verifikasi V5 (crime-inventory portion)**

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
# Cek jumlah baris slide unik = 32 (atau dijelaskan jika ada slide tidak dapat diaudit)
grep -E '^\| 0[1-9]|^\| [12][0-9]|^\| 3[0-2]' analysis/winston-audit/crime-inventory.md | awk -F'|' '{print $2}' | sort -u | wc -l
```

Expected: `32` atau penjelasan eksplisit di file untuk slide yang dikecualikan.

- [ ] **Step 6: Commit**

```bash
git add analysis/winston-audit/crime-inventory.md
git commit -m "audit(winston): per-slide crime inventory for deck v5

Tabel 32 slide x 7 design crimes dengan bukti kutipan/line number,
severity HIGH/MED/LOW, effort S/M/L/XL, dan fix konkret. Memenuhi
spec V5 acceptance: tidak ada penilaian subjektif tanpa dasar; semua
klaim mengutip lokasi konkret di v5.html. Executive summary
mencantumkan agregat per kategori dan flag HIGH-XL untuk E4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 7: Sintesis `analysis/winston-audit/revision-priorities.md`

**Files:**
- Create: `analysis/winston-audit/revision-priorities.md`
- Read: `analysis/winston-audit/crime-inventory.md` (input)

- [ ] **Step 1: Tulis dokumen dengan skeleton berikut**

```markdown
# Winston Revision Priorities — Deck v5 → v6

**Source:** `crime-inventory.md`
**Output target:** `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html`
**E4 escalation rule:** HIGH-XL diangkat ke Phase 4 redesign, bukan patch v6.

---

## Tier 1 — HIGH (Must-Fix Sebelum Demo)

Defect yang merusak kredibilitas atau pemahaman audiens. Wajib dibereskan
di v6 sebelum file dapat dipresentasikan.

| Slide # | Crime # | Bukti | Effort | Fix | E4 Flag |
|---------|---------|-------|--------|-----|---------|
| ... | ... | ... | ... | ... | (kosong / "needs full redesign") |

**Subtotal HIGH:** NN entries (NN dengan E4 flag).

---

## Tier 2 — MEDIUM (Fix di v6, Tidak Mendesak)

Defect yang mengurangi efektivitas tetapi tidak fatal. Diperbaiki di v6
saat tahap eksekusi.

[Tabel sama seperti Tier 1]

---

## Tier 3 — LOW (Kosmetik)

Defect minor — boleh ditunda atau dibiarkan jika effort lebih besar dari
manfaat.

[Tabel sama seperti Tier 1]

---

## E4 Escalation Summary

Daftar entri HIGH-XL yang TIDAK akan di-patch di v6, melainkan diangkat
ke spec untuk Phase 4 redesign:

| Slide # | Crime # | Alasan E4 | Spec Reference |
|---------|---------|------------|-----------------|
| ... | ... | ... | ... |

---

## Recommended Execution Order untuk Phase 4

1. [Tier 1 entries non-XL — fix dulu, biaya/manfaat tertinggi]
2. [Tier 1 entries XL — diangkat ke spec, redesign]
3. [Tier 2]
4. [Tier 3 jika waktu cukup]
```

- [ ] **Step 2: Verifikasi V5 (priorities portion)**

- Setiap entri di crime-inventory dengan severity HIGH muncul di Tier 1.
- Setiap entri HIGH-XL juga muncul di "E4 Escalation Summary".
- Total entri di tiga tier = total entri di crime-inventory (tidak ada yang hilang).

- [ ] **Step 3: Commit**

```bash
git add analysis/winston-audit/revision-priorities.md
git commit -m "audit(winston): revision priorities + E4 escalation list

Tier 1 (HIGH) / 2 (MED) / 3 (LOW) berdasarkan severity di
crime-inventory.md. Entries HIGH-XL diflag terpisah per E4 untuk
redesign Phase 4, bukan patch v6. Mencantumkan recommended execution
order untuk eksekutor Phase 4.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 8: Tulis `analysis/winston-audit/audit-deck-v5.md` (Naratif)

**Files:**
- Create: `analysis/winston-audit/audit-deck-v5.md`
- Read: `analysis/winston-audit/crime-inventory.md` (input data)
- Read: `.claude/winston-framework.md` (untuk evaluasi F1, F3, F4 deck-level)
- Read: `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html` (untuk evaluasi deck-level)

- [ ] **Step 1: Tulis dokumen dengan skeleton berikut**

```markdown
# Winston Framework Audit — Deck v5 (Narrative)

**Audit date:** YYYY-MM-DD
**Source file:** `Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html`
**Companion docs:**
- `crime-inventory.md` — tabel slide × crime
- `revision-priorities.md` — tier HIGH/MED/LOW
- `delivery-checklist.md` — delivery crimes presenter

**Cakupan naratif:** Evaluasi v5 terhadap kelima framework Winston (F1–F5)
dengan bukti konkret. Mencakup area di mana v5 sudah selaras dan area
yang melanggar — bukan hanya defect.

---

## F1 — Start Right Audit

### Apa yang sudah selaras:

[Sebut apa yang v5 sudah lakukan dengan benar di slide 1–3, jika ada.
Bukti: kutipan/line number dari v5.html.]

### Pelanggaran ditemukan:

[Sebut pelanggaran F1 spesifik di v5. Bukti wajib.]

### Rekomendasi:

[Spesifik, mengarah ke fix di crime-inventory.md.]

---

## F2 — Slide Crimes Audit (Ringkasan)

> Detail per-slide ada di `crime-inventory.md`. Bagian ini hanya naratif
> agregat.

**Crime paling sering muncul:** [Sebutkan crime # dengan total tertinggi.]

**Slide paling bermasalah:** [Sebutkan 3 slide dengan jumlah crime
terbanyak.]

**Pola sistemik:** [Pola yang muncul di banyak slide — mis. "Font <40pt
muncul di 24/32 slide; ini bukan defect lokal melainkan systemic
typography choice yang perlu redesign global per E4."]

---

## F3 — STAR Audit

### Symbol

[Apakah v5 punya Symbol yang dapat dikenali? Jika ya, deskripsikan; jika
tidak, sebut sebagai gap.]

### Slogan

[Apakah ada frasa pendek yang diulang? Jika ya, kutipan; jika tidak, gap.]

### Surprise

[Apakah ada klaim kontra-intuitif? Bukti.]

### Salient Idea

[Apakah satu salient idea jelas? Atau v5 menyebar ke 5 ide?]

### Story

[Apakah ada arc narasi? Bukti.]

---

## F4 — Persuade Structure Audit

### Vision Statement

[Apakah established dalam 5 menit pertama? Bukti.]

### Proof of Work

[Apakah spesifik atau vague? Bukti.]

### Opening-Close Mirror

[Apakah opening dan close mirror? Atau close adalah "Terima Kasih"?]

### Contributions Close

[Apakah ada slide kontribusi konkret? Atau slide penutup adalah crime
#9/#10?]

---

## F5 — Props & Stories Audit (Slide Kasus + Konsep Sulit)

### Slide kasus INDF

[Identifikasi slide-slide kasus INDF. Apakah angka disajikan sebagai
prop dengan story arc? Atau tabel polos?]

### Slide konsep sulit

[Identifikasi slide konsep sulit (mis. faithful representation, going
concern). Apakah ada prop atau hanya definisi tekstual?]

---

## Kesimpulan Naratif

[2–3 paragraf merangkum: posisi v5 secara keseluruhan, defect
fundamental, kekuatan yang dipertahankan, dan arah revisi v6/Phase 4
redesign.]
```

- [ ] **Step 2: Isi setiap section dengan bukti konkret**

Setiap klaim "v5 melanggar X" wajib disertai kutipan teks atau line
number di v5.html. Tidak boleh ada penilaian subjektif tanpa dasar.

Penting: jangan hanya menulis defect. Spec V5 mensyaratkan **menyebut area
yang sudah selaras** juga.

- [ ] **Step 3: Verifikasi V5 (narrative portion)**

- Lima framework F1–F5 masing-masing punya section dengan "Apa yang
  sudah selaras" dan "Pelanggaran ditemukan".
- Setiap pelanggaran dikutip lokasi/teks dari v5.html.
- Kesimpulan naratif ada.

- [ ] **Step 4: Commit**

```bash
git add analysis/winston-audit/audit-deck-v5.md
git commit -m "audit(winston): narrative deck audit (F1-F5)

Naratif per framework dengan bukti kutipan/lokasi dari v5.html.
Mencakup area v5 yang sudah selaras dengan Winston dan area yang
melanggar — per spec V5 acceptance. Aggregate referensi ke
crime-inventory.md dan revision-priorities.md untuk detail per-slide.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Task 9: Tulis `analysis/winston-audit/delivery-checklist.md`

**Files:**
- Create: `analysis/winston-audit/delivery-checklist.md`
- Read: `.claude/winston-framework.md` (F2 crimes #4, #5, #6)

- [ ] **Step 1: Tulis dokumen dengan skeleton berikut**

```markdown
# Winston Delivery Checklist — Catatan Presenter

**Source:** F2 Slide Crimes #4, #5, #6 (delivery crimes per E2).
**Audience:** Presenter Group 3 PKK pada hari demo.
**Cakupan:** Crimes yang TIDAK dapat diaudit dari file HTML; hanya
dapat dinilai saat presentasi langsung.

---

## Crime #4 — Membaca Slide

**Aturan Winston:** Jangan membaca slide kata-per-kata. Slide adalah
condiment, bukan main event. Jika audiens dapat membaca slide,
mereka tidak butuh presenter.

**Praktik untuk Group 3:**
- [ ] Setiap presenter berlatih dengan slide tertutup; gunakan slide
      hanya sebagai trigger, bukan teleprompter.
- [ ] Catatan presenter (di pptx notes / kertas terpisah) lebih panjang
      dari isi slide. Body slide = headline + bukti; narasi = catatan.
- [ ] Latihan minimal 2× full run-through sebelum demo.

---

## Crime #5 — Laser Pointer

**Aturan Winston:** Hindari laser pointer — memutus kontak mata dengan
audiens, dan biasanya menandai bahwa slide terlalu kompleks.

**Praktik untuk Group 3:**
- [ ] Tidak menggunakan laser pointer.
- [ ] Bila perlu menandai elemen visual, gunakan animasi build-in
      (highlight muncul saat klik) — disiapkan saat build slide, bukan
      improvisasi.
- [ ] Bila slide perlu pointer karena terlalu padat, itu signal slide
      perlu split (rujuk kembali ke F2 #1, #2).

---

## Crime #6 — Presenter Berdiri Jauh dari Slide

**Aturan Winston:** Presenter berdiri DI samping slide, bukan di
podium yang jauh. Audiens menonton presenter, bukan slide.

**Praktik untuk Group 3:**
- [ ] Cek venue sebelum demo: tahu di mana laptop/proyektor berada.
- [ ] Posisi default: 1–2 langkah dari slide.
- [ ] Hindari berdiri di belakang podium yang jauh dari slide.

---

## Pre-Demo Checklist (1 jam sebelum presentasi)

- [ ] Semua presenter sudah run-through ≥2×.
- [ ] Catatan presenter siap (cetak atau tablet).
- [ ] Tidak ada laser pointer di tas.
- [ ] Posisi berdiri sudah diatur di venue.
- [ ] Empowerment Promise dihafal (slide 1, 60 detik pertama).
- [ ] Slogan deck dihafal (target diucapkan ≥3× selama presentasi).
- [ ] Slide kontribusi (slide 30–32) tetap di layar saat Q&A — TIDAK
      diganti ke "Terima Kasih".
```

- [ ] **Step 2: Verifikasi V5 (delivery portion)**

- Tiga delivery crimes (#4, #5, #6) masing-masing punya section.
- Setiap section memuat aturan Winston + praktik konkret untuk Group 3.
- Pre-demo checklist ada.

- [ ] **Step 3: Commit**

```bash
git add analysis/winston-audit/delivery-checklist.md
git commit -m "audit(winston): delivery crimes checklist for presenters

Crimes #4 (reading), #5 (laser), #6 (distance) dengan praktik konkret
untuk presenter Group 3. Per E2: dipisah dari crime-inventory.md
karena hanya dapat dinilai saat presentasi langsung. Termasuk
pre-demo checklist 1 jam sebelum demo.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## Final Verification (V7)

Setelah Task 1–9 selesai, jalankan checklist akhir spec V7:

- [ ] **V1** — `.claude/winston-framework.md` lengkap (5 framework, label, tabel mapping, no placeholder)
- [ ] **V2** — `specs/presentation-design-spec.md` lengkap (Empowerment, STAR, Vision, Close, struktur 32 slide)
- [ ] **V3** — `specs/winston-integration-rules.md` lengkap (E1 tegas, E2–E5, mapping framework × fase)
- [ ] **V4** — `rubrics/_template.md` lengkap (front-matter, 7 design crimes, F5 trigger, STAR slot)
- [ ] **V5** — Audit deck v5 lengkap (4 file: crime-inventory, revision-priorities, audit-deck-v5, delivery-checklist)
- [ ] **V6** — `v6-winston.html` byte-identik dengan v5 (`md5sum` match)
- [ ] **V7** — Semua 9 commit ter-push ke git; spec disetujui pengguna; tidak ada placeholder tersisa.

```bash
cd "D:/DZAKI/S2/Sem. 1/Pelaporan Keuangan Korporat"
git log --oneline -15
md5sum "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v5 (1).html" \
       "Pelaporan Keuangan Korporat Gr. 3/Pelaporan Keuangan Korporat Gr3 v6-winston.html"
```

Expected:
- 9 commit baru di log dengan prefix `docs(winston)`, `feat(deck)`, `audit(winston)`.
- Dua MD5 hash identik.

---

## Yang BUKAN Bagian dari Plan Ini (Scope Boundary)

- ❌ Modifikasi konten `v6-winston.html` (revisi Winston aktual) — itu pekerjaan plan terpisah `executing-plans` setelah audit selesai.
- ❌ Pembuatan `rubrics/slide-01.md` … `slide-32.md` — itu pekerjaan Phase 3 lanjutan setelah Winston terintegrasi.
- ❌ Phase 1 brainstorming Group 3 deck penuh — Winston *memberi bahan* untuk Phase 1, tetapi Phase 1 sendiri adalah brainstorm terpisah.
- ❌ Modifikasi `sources/group-work-original/` — selamanya read-only.
