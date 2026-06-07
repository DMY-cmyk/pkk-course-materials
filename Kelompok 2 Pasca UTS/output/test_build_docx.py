"""Tests for the markdown parsing layer of build_docx.py."""
from build_docx import parse_inline_runs, parse_blocks, split_caption


def test_plain_text_single_run():
    assert parse_inline_runs("kas adalah kas") == [("kas adalah kas", False, False)]


def test_italic_run():
    assert parse_inline_runs("konsep *quality of income* penting") == [
        ("konsep ", False, False),
        ("quality of income", False, True),
        (" penting", False, False),
    ]


def test_bold_run():
    assert parse_inline_runs("**SFAS No. 95** berlaku 1987") == [
        ("SFAS No. 95", True, False),
        (" berlaku 1987", False, False),
    ]


def test_blocks_heading_para_bullet():
    md = "# Judul\n\n## I. Pendahuluan\n\nParagraf baris satu\nlanjutan baris dua.\n\n- butir pertama\n"
    assert parse_blocks(md) == [
        ("heading", "I. Pendahuluan"),
        ("para", "Paragraf baris satu lanjutan baris dua."),
        ("bullet", "butir pertama"),
    ]


def test_blocks_daftar_pustaka_switches_to_ref():
    md = "## Daftar Pustaka\n\nWolk, H. I. (2017). *Accounting theory*. SAGE.\n"
    assert parse_blocks(md) == [
        ("heading", "Daftar Pustaka"),
        ("ref", "Wolk, H. I. (2017). *Accounting theory*. SAGE."),
    ]


def test_image_block():
    md = "![Gambar 1. Judul Diagram | Sumber: Wolk (2017)](../assets/x.png)\n"
    assert parse_blocks(md) == [
        ("image", ("Gambar 1. Judul Diagram | Sumber: Wolk (2017)", "../assets/x.png")),
    ]


def test_image_block_between_paragraphs():
    md = "Paragraf satu.\n\n![Gambar 2. Judul](../assets/y.png)\n\nParagraf dua.\n"
    assert parse_blocks(md) == [
        ("para", "Paragraf satu."),
        ("image", ("Gambar 2. Judul", "../assets/y.png")),
        ("para", "Paragraf dua."),
    ]


def test_split_caption_with_source():
    assert split_caption("Gambar 1. Judul | Sumber: Wolk (2017)") == (
        "Gambar 1. Judul", "Sumber: Wolk (2017)")


def test_split_caption_without_source():
    assert split_caption("Gambar 2. Judul saja") == ("Gambar 2. Judul saja", None)
