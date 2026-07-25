from app.api.middleware import setup_middleware
from fastapi import FastAPI
import uvicorn

from app.api.routes import router

app = FastAPI(
    title="Personal Finance Agent",
)

setup_middleware(app)


def run():
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


app.include_router(router)
