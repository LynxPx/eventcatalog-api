# Main FastAPI application entry point
# Initialize the FastAPI application.
# Register the GraphQL schema with FastAPI using Strawberry’s FastAPI integration.
# Set up routing, middleware, and any other FastAPI configurations.
import logging

from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from eventcatalog_api.app.db.neo4j import get_neo4j_db
from eventcatalog_api.app.graphql.schema import schema_handler
from eventcatalog_api.server.middleware import CustomHeaderMiddleware

from .config import settings
from .routes.additional_routes import router as additional_routes_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(CustomHeaderMiddleware)

# Register Strawberry GraphQL with FastAPI
graphql_app = GraphQLRouter(schema_handler)


# Ensure that the request object is available in the Strawberry context.
@app.middleware("http")
async def add_request_to_context(request: Request, call_next):
    response = await call_next(request)
    request.state.context = {"request": request}
    return response


app.include_router(graphql_app, prefix="/graphql")

# Example of adding additional routes (RESTful endpoints)
# from app.fastapi.routes.users import router as users_router
# app.include_router(users_router, prefix="/users")

# Include the additional routes
app.include_router(additional_routes_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=settings.port)
