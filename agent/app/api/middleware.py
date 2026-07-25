from app.config import get_conf
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            get_conf().cors_allow_origin,
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
