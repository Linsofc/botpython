# 🤖 Lins PY Bot

Lins PY Bot adalah bot yang dapat berjalan di platform Telegram dan WhatsApp (fitur WhatsApp masih dalam pengembangan). Bot ini dibuat menggunakan Python dengan berbagai modul seperti `rich`, `requests`, dan `python-telegram-bot`.

## ✨ Fitur Utama
- 🚀 **Bot Telegram**
  - `/start` - Memulai bot dan memberikan sapaan
  - `/help` - Menampilkan daftar perintah yang tersedia
  - `/infogempa` - Menampilkan informasi gempa terkini dari BMKG
  - **Menerima dan menampilkan pesan yang diterima dalam format konsol**
- 🔄 **Tampilan Interaktif**
  - Menampilkan banner dengan `pyfiglet`
  - Animasi loading dan efek mengetik menggunakan `rich`
- 🛠 **Koneksi Token Otomatis**
  - Bot akan meminta token Telegram jika tidak ditemukan dalam environment variables

## 📌 Persyaratan
Sebelum menjalankan bot, pastikan Anda memiliki:
- Python 3.x terinstal
- Modul yang diperlukan: `requests`, `rich`, `python-telegram-bot`
- Token bot Telegram yang valid

## 🔧 Instalasi & Penggunaan
1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/Linsofc/botpython.git
   cd botpython

2. **Instal Dependensi**
   ```bash
   pip install requests rich python-telegram-bot pyfiglet

3. **Jalankan Bot**
   ```bash
   python index.py

