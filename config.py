from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from fastapi import FastAPI
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


