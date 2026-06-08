# chapter_locator

Locates the Chapter 12 ("The Income Statement") page range in the Wolk
*Accounting Theory* 9th ed. SAGE-Knowledge PDF and writes
`extraction/chapter-range.json`.

## Result (ground truth, verified)

```
chapter range: pages 305-338 -> extraction/chapter-range.json
```

Chapter 12 occupies **PDF pages 305–338** (1-based, 34 pages). The following
chapter's body begins at page 340 (its title page is 339).

## Why the markers are `Page 2 of <m>`, not chapter titles

This SAGE-Knowledge edition stitches each chapter together as a self-contained
sub-document. The chapter title and body text are rendered with embedded fonts
that carry **no `ToUnicode` CMap**, so `lopdf::Document::extract_text` returns
nothing for them — searching for `"The Income Statement"`, `"Chapter"`,
`"Contributors"`, `"SAGE"`, etc. matches **zero** pages.

The only text that reliably extracts on every page is the per-chapter running
footer `Page <n> of <m>`. Each chapter's own title page (footer `Page 1 of m`)
also extracts as an **empty** page. So:

| Marker          | Unique page | Meaning                                  |
|-----------------|-------------|------------------------------------------|
| `Page 2 of 34`  | 306         | 2nd page of the 34-page Ch.12            |
| `Page 34 of 34` | 338         | last page of Ch.12                       |
| `Page 2 of 31`  | 340         | 2nd page of the following 31-page chapter|

`find_chapter_bounds` locates the two `Page 2 of <m>` anchors (306 and 340),
then `--title-page-offset` (default **1**) shifts each anchor back to its
chapter's empty title page: start `306 - 1 = 305`, end `(340 - 1) - 1 = 338`.

## Run

```powershell
cargo run --release -p chapter_locator
```

Override markers/offset if the edition differs:

```powershell
cargo run --release -p chapter_locator -- --start-marker "Page 2 of 34" --next-marker "Page 2 of 31" --title-page-offset 1
```

`--inspect <1-based-page>` dumps the extracted text of one page for debugging.

## Tests

```powershell
cargo test -p chapter_locator   # 4 passed
```
