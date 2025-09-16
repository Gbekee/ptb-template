from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from bot_handlers.start import start


# Create bot application
tg_app = Application.builder().token(BOT_TOKEN).build()

# Register handlers
tg_app.add_handler(CommandHandler("start", start))

