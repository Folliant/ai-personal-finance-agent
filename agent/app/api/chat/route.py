import random
import time

from fastapi import APIRouter

from app.config import get_conf
from app.api.chat.schemas import (
    ChatRequest,
    ChatResponse,
)
from app.bootstrap import create_orchestrator

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)


orchestrator = create_orchestrator()


@router.post("")
def chat(
    request: ChatRequest,
) -> ChatResponse:
    if get_conf().llm_provider == "mock":
        time.sleep(random.uniform(2, 4))

    try:
        result = orchestrator.run(
            session_id=request.session_id,
            request=request.message,
        )

    except ValueError as e:
        return ChatResponse(
            answer=str(e),
        )

    if result is None:
        return ChatResponse(
            answer="Unable to generate a response.",
        )

    return ChatResponse(
        answer=result,
    )
