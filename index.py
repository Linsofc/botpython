import os
import time
import sys
import requests
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from pyfiglet import Figlet
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

console = Console()

fig = Figlet(font="slant")
banner_text = fig.renderText("Lins PY")
console.print(Align.center(Text(banner_text, style="bold cyan")))

console.print(Panel("[bold yellow]Silakan Pilih Bot yang Ingin Anda Jalankan:[/]", expand=False))
console.print("[bold green]1. Bot Telegram[/]")
console.print("[bold blue]2. Bot WhatsApp[/]")

choice = Prompt.ask("\nMasukkan Pilihan (1/2)", choices=["1", "2"])

if choice == "1":
    
    def get_valid_token():
        while True:
            token = os.getenv("TELEGRAM_BOT_TOKEN")
            if not token:
                console.print("[yellow]⚠ Token tidak ditemukan! Masukkan Token Bot Telegram Anda:[/]")
                token = input("🎟️ Silahkan Masukkan Token: ")
            
            typing_effect("🔍 Memeriksa Token Anda...", 0.05)
            
            if ":" in token:
                console.print("[bold green]Token Berhasil Terhubung[/]")
                return token
            else:
                console.print(Panel("[bold red]❌ Token tidak valid.[/]", border_style="white"))

    def typing_effect(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    TOKEN = get_valid_token()

    with Progress(
        SpinnerColumn(), 
        TextColumn("[progress.description]{task.description}"), 
        BarColumn(), 
        expand=True
    ) as progress:
        task = progress.add_task("[bold blue]Bot Telegram Lins PY Sedang Mencari Koneksi...", total=100)
        for _ in range(10):
            time.sleep(0.3)
            progress.update(task, advance=10)

    console.print(Panel("[bold green]Bot Telegram Lins PY Berhasil Dijalankan.[/]", expand=False, border_style="white"))

    async def start(update: Update, context):
        await update.message.reply_text("Halo! Selamat Datang di Lins PY.\n\nGunakan /help untuk melihat daftar perintah.")

    async def help_command(update: Update, context):
        await update.message.reply_text("📌 Gunakan perintah berikut:\n/start - Memulai Bot\n/help - Menampilkan Menu\n/infogempa - Menampilkan Info Gempa BMKG")

    async def get_gempa():
        url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
        urlGempa = "https://data.bmkg.go.id/DataMKG/TEWS/"
        try:
            response = requests.get(url, timeout=5)
            data = response.json()
            gempa = data["Infogempa"]["gempa"]
            
            pesan = (
                f"Informasi Gempa Saat Ini BMKG\n\n"
                f"Lokasi: {gempa['Wilayah']}\n"
                f"Magnitudo: {gempa['Magnitude']}\n"
                f"Waktu: {gempa['Tanggal']} - {gempa['Jam']}\n"
                f"Koordinat: {gempa['Lintang']} {gempa['Bujur']}\n"
                f"Kedalaman: {gempa['Kedalaman']}\n"
                f"Potensi: {gempa['Potensi']}\n"
            )

            image_url = urlGempa + gempa["Shakemap"] 
            return image_url, pesan
        except Exception as e:
            return None, f"❌ Gagal mengambil data gempa: {str(e)}"

    async def infogempa(update: Update, context):
        image_url, caption = await get_gempa()

        if image_url:
            await update.message.reply_photo(photo=image_url, caption=caption)
        else:
            await update.message.reply_text(caption)

    async def handle_message(update: Update, context):
        """Menampilkan pesan yang diterima dalam format yang diinginkan."""
        user = update.message.from_user
        text = update.message.text

        message_panel = Panel(
            f"[bold cyan]Dari:[/] [bold yellow]{user.first_name}[/]\n\n"
            f"[bold cyan]Pesan:[/] [white]{text}[/]",
            title="[bold green]📩 Pesan Masuk[/]",
            border_style="blue"
        )

        console.print(message_panel)

    def main():
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("infogempa", infogempa))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)) 

        app.run_polling()

    if __name__ == "__main__":
        main()

elif choice == "2":
    console.print(Panel("[bold red]Maaf, fitur ini belum tersedia...[/]", expand=False))


"""
    Create By Lins Official At 07 Februari 2025
"""
