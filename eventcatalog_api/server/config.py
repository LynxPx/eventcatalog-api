# FastAPI configuration settings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Event Catalog API"
    admin_email: str = "ken.cj4@gmail.com"
    version: str = "0.1.0-dev"
    debug_mode: bool = False
    secret_key: str = "secret"
    port: int = 8000
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    neo4j_host: str = "localhost"
    neo4j_port: int = 7687
    neo4j_scheme: str = "bolt"

    class Config:
        env_file = ".env"


settings = Settings()
