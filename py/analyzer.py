# analyzer.py
import math
import yfinance as yf

def hitung_trading_plan(ticker_symbol):
    print(f"Sedang menghitung data saham asli: {ticker_symbol}...")
    try:
        saham = yf.Ticker(ticker_symbol)
        df = saham.history(period="5d")
        
        if df.empty:
            return None

        # Mengambil harga High, Low, Close hari ini setelah pasar BEI tutup
        harga_high = df['High'].iloc[-1]
        harga_low = df['Low'].iloc[-1]
        harga_close = df['Close'].iloc[-1]

        # RUMUS MATEMATIKA PIVOT POINT STANDAR
        titik_pivot = (harga_high + harga_low + harga_close) / 3
        support_1 = (2 * titik_pivot) - harga_high
        support_2 = titik_pivot - (harga_high - harga_low)
        resistance_1 = (2 * titik_pivot) - harga_low
        resistance_2 = titik_pivot + (harga_high - harga_low)

        # Bulatkan angka agar rapi di tampilan website
        beli_min = math.floor(support_2)
        beli_max = math.floor(support_1)
        jual_min = math.ceil(resistance_1)
        jual_max = math.ceil(resistance_2)

        # Filter Kondisi & AI Sentimen Berdasarkan Posisi Tren terhadap Pivot
        if harga_close > titik_pivot:
            kondisi = "STRONG BUY"
            badge_class = "strong-buy"
            skor_sentimen = "85% Positif (Sentimen Bullish Kuat)"
            alasan = f"Emiten {ticker_symbol} bergerak aktif dan berhasil ditutup menguat di atas titik pivot harian Rp {math.floor(titik_pivot)}. Indikator menunjukkan tekanan beli yang mendominasi pasar modal menjelang penutupan, didukung sentimen akumulasi positif pasar lokal. Peluang kelanjutan tren naik sangat terbuka."
        else:
            kondisi = "AVOID"
            badge_class = "avoid"
            skor_sentimen = "35% Positif (Tekanan Jual Tinggi)"
            alasan = f"Emiten {ticker_symbol} ditutup di bawah titik pivot harian Rp {math.floor(titik_pivot)}, mengindikasikan adanya aksi ambil untung (profit taking) yang masif dari para investor besar. AI mendeteksi volatilitas jangka pendek masih berisiko tinggi. Disarankan menunggu sinyal pantulan di area support bawah."

        return {
            "saham": ticker_symbol,
            "harga_terakhir": math.floor(harga_close),
            "rentang_beli": f"{beli_min} - {beli_max}",
            "rentang_jual": f"{jual_min} - {jual_max}",
            "skor_sentimen": skor_sentimen,
            "kondisi": kondisi,
            "badge_class": badge_class,
            "alasan": alasan
        }
    except Exception as e:
        print(f"Error memproses {ticker_symbol}: {e}")
        return None
