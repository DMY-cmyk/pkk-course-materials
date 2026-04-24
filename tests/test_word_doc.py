import pytest


def test_all_modules_import():
    from scripts.word_doc import styles, visuals, cover, front_matter, bibliography
    from scripts.word_doc.sections import (
        bagian_i, bagian_ii, bagian_iii, bagian_iv,
        bagian_v, bagian_vi, bagian_vii, bagian_viii,
    )
