from fastapi import APIRouter, Request
from telegram import Update
from bot import tg_app

webhook_router = APIRouter()

@webhook_router.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, tg_app.bot)
    await tg_app.process_update(update)
    return {"ok": True}
