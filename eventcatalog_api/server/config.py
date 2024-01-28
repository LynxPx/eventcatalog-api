# FastAPI configuration settings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Event Catalog API"
    admin_email: str = "ken.cj4@gmail.com"
    version: str = "0.1.0-dev"
    debug_mode: bool = False
    secret_key: str = "secret"
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
