import requests
import os
TELEGRAM_TOKEN = "8203901193: AAGhC2Hm5GØF_Vj8PY590RCjpI
VITP7p1kw"
CHAT_ID = "6711054848"

def mesaj_gonder(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

def ajan_calistir():
    sonuc = """
🔥 YENİ DİJİTAL ÜRÜN

Ürün: Telefonla İlk Paran
Hedef: Sıfır bilgi
Fiyat: 149 TL

İçerik:
- Para kazanma yolları
- Uygulama listesi
- Günlük plan

Satış metni:
"Hiçbir şey bilmeden sadece telefonla para kazanmak ister misin?"
"""

    mesaj_gonder(sonuc)

if __name__ == "__main__":
    ajan_calistir()
