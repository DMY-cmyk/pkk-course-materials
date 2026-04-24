from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph, add_footnote_text,
)


def build(doc) -> None:
    """Bagian V — Catatan Kritis dan Perspektif Akademis"""

    add_section_heading(doc, "V. CATATAN KRITIS DAN PERSPEKTIF AKADEMIS")

    add_sub_heading(doc, "V.1 SFAC 5 sebagai 'Achilles' Heel': Kritik Solomons")
    add_body_paragraph(
        doc,
        "David Solomons, salah satu arsitek intelektual kerangka konseptual FASB, pada akhirnya "
        "menyebut SFAC 5 sebagai 'Achilles' heel of the FASB's conceptual framework' — sebuah "
        "kritik yang dikutip secara luas oleh Wolk, Dodd & Rozycki (2017, Ch.7). Solomons "
        "berargumen bahwa SFAC 5 pada dasarnya merupakan 'cop-out' — sebuah dokumen yang "
        "mendeskripsikan apa yang sudah dilakukan praktisi, bukan menetapkan apa yang seharusnya "
        "dilakukan. Akibatnya, kerangka konseptual yang seharusnya memberikan panduan normatif "
        "untuk penetapan standar justru menjadi cermin deskriptif dari status quo."
    )
    add_body_paragraph(
        doc,
        "Respons FASB terhadap kritik ini terlihat dalam SFAC 8 Chapter 5 yang memperkenalkan "
        "prinsip cost-benefit sebagai pertimbangan utama dalam pengakuan — sebuah pendekatan "
        "yang lebih normatif. Namun demikian, SFAC 5 tetap berlaku hingga hari ini dan menjadi "
        "referensi bagi standar akuntansi AS yang ada, menciptakan ketegangan antara framework "
        "baru (SFAC 8) dan standar lama yang masih mengacu SFAC 5."
    )

    add_sub_heading(doc, "V.2 Perdebatan Fair Value: Relevansi vs. Reliabilitas dalam Praktik")
    add_body_paragraph(
        doc,
        "Perdebatan tentang Fair Value (nilai wajar) mencerminkan ketegangan abadi antara dua "
        "karakteristik kualitatif: Relevansi dan Faithful Representation. Pendukung Fair Value "
        "berargumen bahwa nilai pasar kini lebih relevan bagi investor karena mencerminkan "
        "kondisi ekonomi terkini, bukan biaya historis yang mungkin sudah usang. Namun "
        "para kritikus mengidentifikasi risiko pro-siklikalitas (pro-cyclicality): pada periode "
        "krisis keuangan, penurunan Fair Value memaksa pengakuan kerugian yang memperbesar "
        "tekanan pada lembaga keuangan, menciptakan spiral negatif yang memperburuk krisis "
        "(bank run → asset write-down → capital shortfall → lebih banyak write-down)."
    )

    add_sub_heading(doc, "V.3 Penghapusan Konservatisme: Implikasi untuk Praktik")
    add_body_paragraph(
        doc,
        "Penghapusan Conservatism dari SFAC 8 (BC3.27–29) merupakan keputusan yang paling "
        "kontroversial dalam sejarah kerangka konseptual FASB. Konservatisme tradisional — "
        "'anticipate no profits, but anticipate all losses' — telah menjadi panduan praktis "
        "akuntansi selama berabad-abad. FASB berargumen bahwa konservatisme sistematis "
        "bertentangan dengan Neutrality (salah satu komponen Faithful Representation) "
        "karena ia mendorong bias ke arah under-statement aset. Namun sejumlah akademisi "
        "mempertanyakan apakah Neutrality tanpa konservatisme justru membuka ruang yang lebih "
        "besar bagi manajemen untuk melakukan income smoothing dan overstatement aset."
    )

    add_sub_heading(doc, "V.4 Implikasi untuk Standard Setter Indonesia")
    add_body_paragraph(
        doc,
        "DSAK-IAI, sebagai adopter IASB CF 2018, mewarisi sekaligus ketegangan-ketegangan "
        "konseptual yang belum sepenuhnya terselesaikan dalam SFAC 8. Tantangan spesifik untuk "
        "konteks Indonesia meliputi: (1) keterbatasan pasar aktif untuk pengukuran Fair Value "
        "aset tertentu, yang mengurangi reliabilitas Exit Price; (2) kompleksitas struktur "
        "konglomerat (seperti INDF dengan empat divisi utama) dalam pengujian impairment "
        "Goodwill; dan (3) ketegangan antara kebutuhan konservatisme untuk perlindungan "
        "kreditur dan tuntutan Neutrality dari kerangka konseptual modern."
    )

    add_footnote_text(
        doc,
        "⁵ Kutipan 'Achilles' heel' dan 'cop-out': Wolk, Dodd & Rozycki (2017), "
        "Accounting Theory: Conceptual Issues in a Political and Economic Environment, "
        "Ch.7, hal. 175. Pro-cyclicality Fair Value: lihat Plantin, Sapra & Shin (2008); "
        "Allen & Carletti (2008)."
    )
