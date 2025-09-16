from config import tg_app
from telegram.ext import CommandHandler
from telegram import Update

async def start(update: Update, context):
    await update.message.reply_text("Hello from FastAPI + PTB Webhook!")

tg_app.add_handler(CommandHandler("start", start))