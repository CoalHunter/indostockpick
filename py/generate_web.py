# generate_web.py
from config import SAHAM_TARGET, dapatkan_html_atas, dapatkan_html_bawah
from analyzer import hitung_trading_plan

def rakit_halaman_statis():
    data_matang = []
    
    # 1. Ambil dan hitung data untuk setiap saham
    for emiten in SAHAM_TARGET:
        plan = hitung_trading_plan(emiten)
        if plan:
            data_matang.append(plan)
            
    # 2. Ambil kerangka HTML bagian atas
    html_content = dapatkan_html_atas()
    
    # 3. Rakit bagian tengah (Kartu Saham & Iklan Tengah Konten)
    for index, item in enumerate(data_matang):
        html_content += f"""
            <div class="stock-card" onclick="openDetailModal({index})">
                <div class="card-header">
                    <h2 class="stock-name">{item['saham']}</h2>
                    <span class="badge {item['badge_class']}">{item['kondisi']}</span>
                </div>
                <div class="price-section">
                    Harga Terakhir: <b>Rp {item['harga_terakhir']}</b>
                </div>
                <div class="zone-container">
                    <div class="buy-zone">
                        🟢 Area Beli
                        <span class="zone-price">{item['rentang_beli']}</span>
                    </div>
                    <div class="sell-zone">
                        🔴 Area Jual
                        <span class="zone-price">{item['rentang_jual']}</span>
                    </div>
                </div>
                <div class="sentiment-bar">
                    🤖 AI Sentimen: <b>{item['skor_sentimen']}</b>
                </div>
            </div>
"""
        # Menyisipkan Iklan Banner Ke-2 (Tengah) tepat setelah kartu kedua
        if index == 1:
            html_content += """
            <div class="ad-container ad-middle">
                <p class="ad-label">SPONSORED ADVERTISEMENT (MIDDLE)</p>
                <div class="ad-mock-content">Slot Iklan Banner Tengah - Di dalam Aliran Konten</div>
            </div>
"""

    # 4. Rakit data array JavaScript untuk kebutuhan Pop-up Detail
    js_array_data = ""
    for item in data_matang:
        aman_alasan = item['alasan'].replace('"', '\\"')
        js_array_data += f"""{{
            saham: "{item['saham']}",
            harga: "{item['harga_terakhir']}",
            kondisi: "{item['kondisi']}",
            badge: "{item['badge_class']}",
            alasan: "{aman_alasan}"
        }},"""

    # 5. Gabungkan dengan HTML bagian bawah dan tulis ke file fisik
    html_content += dapatkan_html_bawah(js_array_data)
    
    with open("../index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("\n[SUKSES] File 'index.html' statis berhasil diperbarui dengan data pasar asli!")

if __name__ == "__main__":
    rakit_halaman_statis()
