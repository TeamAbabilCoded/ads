

# 🧠 Auto Visit & Click Bot with Telegram Report

Script Python otomatis untuk mengunjungi **direct link**, mensimulasikan klik iklan, dan melaporkan statistik harian ke Telegram. Dilengkapi dengan:

* Simulasi kunjungan dari Android/iPhone
* Proxy support (IPv4 public/residential)
* Delay random anti-spam
* Simulasi klik
* Laporan otomatis ke Telegram (via Bot)

---

## 📦 Struktur File

```
ads/
├── main.py
├── config.json
├── proxies.txt
├── user_agents/
│   ├── android.txt
│   └── iphone.txt
├── utils/
│   ├── browser.py
│   ├── logger.py
│   └── telegram.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Persiapan

### 1. Install Python Package

```bash
pip install -r requirements.txt
```

### 2. Isi File `config.json`

```json
{
  "bot_token": "123456:ABC-DEF...",
  "chat_id": "123456789",
  "min_delay": 20,
  "max_delay": 35,
  "click_probability": 0.25,
  "headless": true,
  "use_mobile_useragent": true
}
```

### 3. Tambah Proxy ke `proxies.txt`

Isi dengan format:

```
ip:port
ip:port:user:pass
```

---

## ▶️ Menjalankan Bot

```bash
python main.py
```

Script akan:

* Pilih proxy acak
* Gunakan User-Agent Android/iPhone
* Buka direct link pakai Selenium
* Delay random
* Simulasikan klik dengan probabilitas tertentu
* Kirim laporan ke Telegram

---

## 📤 Contoh Pesan Telegram

```
📊 Daily Visit Report

🕒 Waktu: 2025-07-20 14:00
🔗 URL: https://example.com
📱 Device: Android
🌐 IP: 123.45.67.89
✅ Visit Berhasil
🖱 Klik Simulasi: Ya
```

---

## ❗ Catatan Penting

* Gunakan dengan bijak. Tujuan script ini hanya untuk edukasi dan riset.
* Jangan gunakan untuk spam atau pelanggaran TOS platform iklan manapun.
* Untuk performa maksimal, gunakan proxy ISP atau mobile dari provider seperti BrightData.


