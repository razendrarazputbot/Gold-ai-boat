from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Gold AI Bot Active!\n\n"
        "Commands:\n"
        "/price - Gold price (coming soon)\n"
        "/news - Market news (coming soon)\n"
        "/signal - Trading signal (coming soon)"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Gold price feature coming soon.")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 Market news feature coming soon.")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Signal feature coming soon.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("signal", signal))

print("Gold AI Bot Started...")

app.run_polling()
