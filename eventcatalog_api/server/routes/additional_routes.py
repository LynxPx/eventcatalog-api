import json
import logging

from fastapi import APIRouter, Depends

from eventcatalog_api.app.db.neo4j import get_neo4j_db
from eventcatalog_api.server.config import settings

router = APIRouter()


# Add any middleware, event handlers, etc.
@router.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "version": settings.version,
    }


# Neo4j test
@router.get("/neo4j")
async def run_neo4j_query(db=Depends(get_neo4j_db)):
    return {"message": "Hello Neo4j!"}


@router.get("/neo4j/status")
async def test_neo4j_connection(db=Depends(get_neo4j_db)):
    try:
        return {"message": "Neo4j connection is successful!"}
    except Exception as e:
        return {"message": f"Failed to connect to Neo4j: {e}"}


@router.get("/neo4j/record")
async def get_neo4j_record(db=Depends(get_neo4j_db)):
    try:
        # Query to pull one record from Neo4j
        record = db.cypher_query("MATCH p=()-->() RETURN p LIMIT 1")
        return {"record": record}
    except Exception as e:
        return {"message": f"Failed to retrieve Neo4j record: {e}"}


@router.on_event("startup")
async def startup_event():
    logging.info("Starting the application...")
    try:
        logging.info("Neo4j database connection started.")
    except Exception as e:
        logging.error(f"An error occurred while starting the Neo4j connection: {e}")
    logging.info("Application has started successfully.")


@router.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down the application...")
    try:
        logging.info("Neo4j database connection closed.")
    except Exception as e:
        logging.error(f"An error occurred while closing the Neo4j connection: {e}")
    logging.info("Application has been shut down successfully.")
