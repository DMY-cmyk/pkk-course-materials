import pytest


def test_all_modules_import():
    from scripts.word_doc import styles, visuals, cover, front_matter, bibliography
    from scripts.word_doc.sections import (
        bagian_i, bagian_ii, bagian_iii, bagian_iv,
        bagian_v, bagian_vi, bagian_vii, bagian_viii,
    )


from docx import Document


def test_set_run_font_sets_times_new_roman():
    from scripts.word_doc.styles import set_run_font
    doc = Document()
    p = doc.add_paragraph()
    run = p.add_run("test")
    set_run_font(run, size_pt=12)
    assert run.font.name == "Times New Roman"
    assert run.font.size.pt == 12
    assert run.font.bold is None or run.font.bold is False


def test_add_section_heading_is_14pt_bold():
    from scripts.word_doc.styles import add_section_heading
    doc = Document()
    p = add_section_heading(doc, "I. TEST HEADING")
    run = p.runs[0]
    assert run.font.bold is True
    assert run.font.size.pt == 14


def test_add_body_paragraph_is_12pt():
    from scripts.word_doc.styles import add_body_paragraph
    doc = Document()
    p = add_body_paragraph(doc, "Some text here.")
    run = p.runs[0]
    assert run.font.size.pt == 12
    assert run.font.bold is None or run.font.bold is False


def test_add_table_with_headers_shape():
    from scripts.word_doc.styles import add_table_with_headers
    doc = Document()
    headers = ["Kolom A", "Kolom B", "Kolom C"]
    rows = [["a1", "b1", "c1"], ["a2", "b2", "c2"]]
    table = add_table_with_headers(doc, headers, rows)
    assert len(table.rows) == 3   # 1 header + 2 data
    assert len(table.columns) == 3
