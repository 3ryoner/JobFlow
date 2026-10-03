from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "JobFlow"
    debug: bool = False
    app_env: str = "development"
    # database
    database_url: str = "postgresql+asyncpg://jobflow:jobflow@localhost:5432/jobflow"
    redis_url: str = "redis://localhost:6379/0"
    rabbitmq_url: str = "amqp://jobflow:jobflow@localhost:5672//"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
