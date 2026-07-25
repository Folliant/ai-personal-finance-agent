from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    openai_api_key: str = Field(
        default="",
        min_length=10,
    )
    model: str = Field(
        default="gpt-5.4",
        min_length=1,
    )

    max_tool_iterations: int = Field(
        default=10,
        ge=1,
    )

    cors_allow_origin: str = Field(
        default="http://localhost:5173",
        min_length=1,
    )

    llm_provider: Literal[
        "mock",
        "openai",
    ] = "openai"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_conf() -> Config:
    return Config()
