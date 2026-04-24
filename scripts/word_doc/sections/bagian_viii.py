from scripts.word_doc.styles import (
    add_section_heading, add_sub_heading, add_body_paragraph,
)


def build(doc) -> None:
    """Bagian VIII — Kesimpulan"""

    add_section_heading(doc, "VIII. KESIMPULAN")

    add_sub_heading(doc, "VIII.1 Sintesis: CF sebagai Fondasi Hierarki Standar → Praktik")
    add_body_paragraph(
        doc,
        "Kerangka Konseptual FASB — dalam manifestasinya yang paling mutakhir sebagai SFAC 8 "
        "edisi September 2024 — membuktikan dirinya sebagai fondasi arsitektur yang koheren "
        "dan berjenjang bagi seluruh standar akuntansi modern. Perjalanan dari SFAC 1 (1978) "
        "yang menetapkan tujuan pelaporan keuangan, hingga SFAC 8 September 2024 yang "
        "merevisi definisi aset, kriteria pengakuan, dan panduan pengukuran, mencerminkan "
        "evolusi pemikiran akuntansi yang responsif terhadap kritik akademisi dan tuntutan "
        "praktik pasar global."
    )
    add_body_paragraph(
        doc,
        "Empat perubahan konseptual paling signifikan dalam evolusi ini — (1) pergantian "
        "Reliability dengan Faithful Representation, (2) penurunan status Verifiability, "
        "(3) penghapusan Conservatism, dan (4) redefinisi aset menjadi 'present right' — "
        "secara konsisten menunjukkan arah yang sama: dari orientasi objektivitas-verifikasi "
        "menuju orientasi representasi-realitas-ekonomi. SFAC 8 menempatkan relevansi "
        "ekonomi di atas kemudahan audit, sebuah pilihan konseptual yang terus diperdebatkan "
        "dalam literatur akademik."
    )

    add_sub_heading(doc, "VIII.2 INDF 2024 sebagai Cerminan Teori: Keselarasan dan Gap")
    add_body_paragraph(
        doc,
        "Laporan keuangan PT Indofood Sukses Makmur Tbk 2024 mendemonstrasikan implementasi "
        "kerangka konseptual yang umumnya baik: penyajian NCI yang transparan, pengukuran "
        "aset tetap berbasis Historical Cost (Entry Price) yang konsisten dengan M30, "
        "pengakuan pendapatan yang memenuhi tiga kriteria SFAC 8 Ch.5, dan disclosure Goodwill "
        "yang komprehensif di catatan kaki. Namun terdapat gap yang perlu diperhatikan: "
        "Goodwill sebesar Rp52,2 triliun (26% total aset) mengandalkan asumsi DCF yang "
        "tidak sepenuhnya transparan, menciptakan ketegangan dengan prinsip Faithful "
        "Representation — khususnya dimensi Completeness dan Free from Error."
    )

    add_sub_heading(doc, "VIII.3 Implikasi untuk Standard Setter dan Praktisi Indonesia")
    add_body_paragraph(
        doc,
        "Bagi DSAK-IAI sebagai adopter IASB CF 2018, pemahaman mendalam tentang SFAC 8 "
        "memberikan konteks historis dan konseptual yang berharga. Ketika DSAK-IAI "
        "mempertimbangkan amendemen PSAK — misalnya terkait Goodwill accounting, IFRS 17 "
        "Insurance Contracts, atau IFRS 16 Leases — landasan konseptual SFAC 8 memberikan "
        "kerangka argumentasi yang terstruktur. Bagi OJK sebagai regulator pasar modal, "
        "pemahaman tentang limitasi Fair Value (pro-cyclicality) dan keterbatasan catatan kaki "
        "(D32) dapat menginformasikan kebijakan pengungkapan emiten."
    )
    add_body_paragraph(
        doc,
        "Kesimpulan akhir: studi kasus INDF 2024 menegaskan bahwa kerangka konseptual FASB "
        "bukan sekadar dokumen akademis — ia adalah panduan operasional yang secara langsung "
        "mempengaruhi bagaimana Goodwill Rp52,2 triliun diukur, bagaimana NCI Rp43,077 "
        "triliun diklasifikasikan, dan bagaimana tren EPS Rp984 per saham diinterpretasikan "
        "oleh investor. Memahami fondasi konseptual ini adalah prasyarat untuk memahami "
        "realitas laporan keuangan korporasi modern."
    )
