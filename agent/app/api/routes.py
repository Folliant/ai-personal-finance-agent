from fastapi import APIRouter

from app.api.chat.route import router as chat_router

router = APIRouter()

router.include_router(chat_router)
