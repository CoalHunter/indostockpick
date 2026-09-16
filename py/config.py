# config.py
from datetime import datetime

# Daftar saham Bursa Efek Indonesia yang ingin di-scan otomatis
SAHAM_TARGET = ["BBRI.JK", "TLKM.JK", "ASII.JK", "BMRI.JK", "BBNI.JK", "UNVR.JK"]

def dapatkan_html_atas():
    waktu_sekarang = datetime.now().strftime("%A, %d %b %Y")
    waktu_lengkap = datetime.now().strftime("%A, %d %b %Y - 16:00 WIB")
    
    emiten_keyword = ", ".join([s.replace('.JK', '') for s in SAHAM_TARGET])

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- TAG SEO UTAMA -->
    <title>IndoStockPick: Rekomendasi & Rencana Trading Saham BEI {waktu_sekarang}</title>
    <meta name="description" content="Rekomendasi stockpick saham Indonesia hari ini {waktu_sekarang} berdasarkan analisis teknikal Pivot Point harian dan AI Sentimen untuk emiten {emiten_keyword}.">
    <meta name="keywords" content="stockpick saham, rekomendasi saham hari ini, trading plan saham, analisa teknikal bei, saham {emiten_keyword.lower()}">
    <meta name="robots" content="index, follow">
    
    <!-- OPEN GRAPH -->
    <meta property="og:title" content="IndoStockPick: Rencana Trading Saham BEI Harian">
    <meta property="og:description" content="Analisis teknikal otomatis dan sentimen berita saham Indonesia terupdate setiap sore.">
    <meta property="og:type" content="website">
    
    <link rel="stylesheet" href="style.css">

    <!-- GOOGLE SCHEMA MARKUP -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FinancialProduct",
      "name": "IndoStockPick Harian",
      "description": "Analisis rentang harga beli dan jual saham pilihan di Bursa Efek Indonesia.",
      "brand": {{
        "@type": "Brand",
        "name": "IndoStockPick"
      }}
    }}
    </script>
</head>
<body>
    <header>
        <h1>📈 IndoStockPick</h1>
        <p>Rekomendasi Stockpick Saham Indonesia berbasis Teknikal & AI Sentimen</p>
        <div id="update-time">Update Terakhir: {waktu_lengkap}</div>
    </header>

    <!-- 1. SLOT IKLAN ATAS -->
    <div class="ad-container">
        <p class="ad-label">SPONSORED ADVERTISEMENT (TOP)</p>
        <div class="ad-mock-content">Slot Iklan Banner Atas - Google Adsense</div>
    </div>

    <main>
        <h2 style="text-align:center; font-size:1.2rem; color:#555; margin-bottom:20px;">
            Rencana Trading Plan & Analisis Saham Pilihan Hari Ini
        </h2>
        <div class="grid-container">
"""

def dapatkan_html_bawah(js_array_data):
    return f"""
        </div>
    </main>

    <!-- 2. SLOT IKLAN BAWAH -->
    <div class="ad-container">
        <p class="ad-label">SPONSORED ADVERTISEMENT (BOTTOM)</p>
        <div class="ad-mock-content">Slot Iklan Banner Bawah - Google Adsense</div>
    </div>

    <section class="disclaimer-box">
        <p>⚠️ <b>Pernyataan Risiko (Disclaimer):</b> Semua rekomendasi saham di website ini dihasilkan secara otomatis oleh analisis teknikal dan AI sentimen untuk tujuan edukasi. Ini <b>bukan ajakan resmi</b> untuk membeli atau menjual saham. Keputusan investasi sepenuhnya ada di tangan Anda. <a href="#" id="open-modal">Baca Selengkapnya (Terms & Conditions)</a> | <a href="privacy-policy.html">Kebijakan Privasi</a></p>
    </section>

    <!-- POP-UP DISCLAIMER YANG SUDAH DILENGKAPI INSIGHT & SCROLL -->
    <div id="disclaimer-modal" class="modal">
        <div class="modal-content">
            <span class="close-btn" id="close-disclaimer">&times;</span>
            <h2>Pasal Sanggahan & Ketentuan Layanan (Disclaimer Terms)</h2>
            <hr>
            <div class="modal-body">
                <div class="modal-risk-alert">
                    💡 Alat bantu navigasi untuk trader ritel agar terhindar dari transaksi emosional (Feelingmology).
                </div>
                <ol>
                    <li><b>Bukan Nasihat Keuangan:</b> Konten, data, rentang harga, dan skor sentimen murni hasil algoritma komputer dan kecerdasan buatan (AI). Kami tidak menyediakan jasa penasihat investasi berlisensi.</li>
                    <li><b>Risiko Investasi (DYOR):</b> Pasar saham memiliki risiko volatilitas tinggi. Kerugian finansial yang Anda alami akibat mengikuti trading plan di website ini adalah <b>tanggung jawab mutlak Anda sendiri</b>. Wajib pelajari dan analisis ulang sebelum membeli!</li>
                    <li><b>Dilarang Keras ALL IN:</b> Memasukkan seluruh modal ke dalam satu saham tunggal adalah tindakan spekulasi yang sangat berbahaya, apa pun alasannya. Kehilangan modal kerja dapat menghancurkan portofolio ritel dalam sekejap.</li>
                    <li><b>Alokasi Budget Aman (10% - 20%):</b> Gunakan hanya <b>10% hingga 20% dari total budget trading</b> Anda untuk satu emiten saham. Langkah ini memperkecil risiko modal tersangkut, sekaligus menyisakan ruang dana tunai untuk melakukan strategi <i>Average Down</i> (pembelian rata-rata bawah) jika sistem di hari berikutnya mengeluarkan sinyal akumulasi beli yang sangat kuat.</li>
                    <li><b>Disiplin Pembatasan Risiko:</b> Selalu siapkan batas toleransi penurunan harga (Cut Loss mandiri) secara ketat sebelum bertransaksi demi mengamankan sisa modal dalam jangka panjang.</li>
                    <li><b>Kendalikan Psikologi (Anti-FOMO):</b> Bursa Efek Indonesia buka sepanjang tahun. Jangan memaksakan diri membeli saham yang sudah terbang terlalu tinggi hanya karena takut tertinggal kereta (*Fear of Missing Out*).</li>
                    <li><b>Akurasi Data:</b> Kami tidak menjamin 100% keakuratan data karena adanya potensi delay atau gangguan teknis dari penyedia data pasar.</li>
                </ol>
            </div>
        </div>
    </div>

    <div id="detail-modal" class="modal">
        <div class="modal-content">
            <span class="close-btn" id="close-detail">&times;</span>
            <h2 id="modal-stock-title">Detail Analisis</h2>
            <hr>
            <div class="modal-body">
                <p><b>Harga Saat Ini:</b> <span id="modal-stock-price"></span></p>
                <p><b>Rekomendasi Aksi:</b> <span id="modal-stock-badge" class="badge"></span></p>
                <div class="analysis-box">
                    <h3>🔍 Mengapa Saham Ini Direkomendasikan?</h3>
                    <p id="modal-stock-reason"></p>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 IndoStockPick. All Rights Reserved. | <a href="privacy-policy.html" style="color: #7f8c8d; text-decoration: underline;">Privacy Policy</a></p>
    </footer>

    <script>
        const DATA_ANALISIS = [{js_array_data}];

        function openDetailModal(index) {{
            const item = DATA_ANALISIS[index];
            document.getElementById("modal-stock-title").innerText = "Analisis Mendalam: " + item.saham;
            document.getElementById("modal-stock-price").innerText = "Rp " + item.harga;
            document.getElementById("modal-stock-reason").innerText = item.alasan;
            
            const badge = document.getElementById("modal-stock-badge");
            badge.innerText = item.kondisi;
            badge.className = "badge " + item.badge;
            
            document.getElementById("detail-modal").style.display = "block";
        }}

        document.addEventListener("DOMContentLoaded", () => {{
            const dModal = document.getElementById("disclaimer-modal");
            const dtModal = document.getElementById("detail-modal");
            
            document.getElementById("open-modal").addEventListener("click", (e) => {{
                e.preventDefault(); dModal.style.display = "block";
            }});
            document.getElementById("close-disclaimer").addEventListener("click", () => {{
                dModal.style.display = "none";
            }});
            document.getElementById("close-detail").addEventListener("click", () => {{
                dtModal.style.display = "none";
            }});
            window.addEventListener("click", (e) => {{
                if (e.target === dModal) dModal.style.display = "none";
                if (e.target === dtModal) dtModal.style.display = "none";
            }});
        }});
    </script>
</body>
</html>

