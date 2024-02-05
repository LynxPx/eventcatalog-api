# app/db/neo4j.py

import logging

from neomodel import config, db
from pydantic_settings import BaseSettings


# Define Neo4j settings using Pydantic's BaseSettings
class Neo4jSettings(BaseSettings):
    scheme: str = "bolt"
    host: str = "localhost"
    port: str = "7687"
    user: str = "neo4j"
    password: str = "password"

    def get_database_url(self):
        return f"{self.scheme}://{self.user}:{self.password}@{self.host}:{self.port}"

    class Config:
        env_file = ".env"
        env_prefix = "NEO4J_"


# Instantiate settings from environment variables or defaults
neo4j_settings = Neo4jSettings()

# Set up the connection URL for neomodel
config.DATABASE_URL = neo4j_settings.get_database_url()
logging.info(f"Neo4j database URL: {config.DATABASE_URL}")


# Dependency for FastAPI to yield a neomodel db instance
def get_neo4j_db():
    try:
        logging.info("Opening connection to Neo4j database")
        # Here you can perform any setup actions if needed before yielding db
        yield db
    finally:
        logging.info("Closing connection to Neo4j database")
        # Here you can perform any teardown or cleanup actions if needed
        pass
