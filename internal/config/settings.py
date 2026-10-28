from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CheckIn Backend Service"
    app_version: str = "1.0.0"
    host: str = "127.0.0.1"

    port: int = Field(default=8000, validation_alias=AliasChoices("HTTP_PORT", "PORT"))

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
