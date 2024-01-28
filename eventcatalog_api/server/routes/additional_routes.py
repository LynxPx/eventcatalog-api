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
    # results, meta = db.cypher_query("MATCH (n) RETURN n")
    # return results


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
