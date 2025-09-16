import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import WEBHOOK_URL
from bot import tg_app
from webhook import webhook_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await tg_app.initialize()
    await tg_app.bot.set_webhook(WEBHOOK_URL)
    yield
    await tg_app.shutdown()

api_app = FastAPI(lifespan=lifespan)

# Mount webhook routes
api_app.include_router(webhook_router)

if __name__ == "__main__":
    uvicorn.run(api_app, host="0.0.0.0", port=8000)
