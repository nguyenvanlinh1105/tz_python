from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    PROJECT_NAME: str = "Todo API"

    class Config:
        env_file = ".env"


settings = Settings()
