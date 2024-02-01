"""
schema.py  is the main GraphQL schema in a FastAPI project using Strawberry GraphQL should define the root Query, Mutation, and possibly Subscription types, which are entry points for the GraphQL API. The schema brings together all of the individual GraphQL type definitions and resolvers from different domains.
"""

import json
from typing import List

import strawberry

from eventcatalog_api.app.graphql.types.badge import Badge
from eventcatalog_api.app.graphql.types.main import Domain, Event, Service
from eventcatalog_api.app.graphql.types.owner import Owner
from eventcatalog_api.app.graphql.types.repository import Repository
from eventcatalog_api.app.graphql.types.schema import Schema
from eventcatalog_api.app.graphql.types.tag import Tag
from eventcatalog_api.app.graphql.types.user import User

from .fetchers.mock_data_fetcher import (
    fetch_badges_list,
    fetch_domains_list,
    fetch_events_list,
    fetch_owners_list,
    fetch_repository_list,
    fetch_schema_list,
    fetch_services_list,
    fetch_tags_list,
    fetch_users_list,
)


@strawberry.type
class Query:
    @strawberry.field
    def badges(self, info, limit: int = 1) -> List[Badge]:
        # Create instances of Badge
        badges_lst = fetch_badges_list(limit)
        return badges_lst[:limit]

    @strawberry.field
    def domains(self, info, limit: int = 1) -> List[Domain]:
        # Create instances of Domain
        domains_lst = fetch_domains_list(limit)
        return domains_lst[:limit]

    @strawberry.field
    def events(self, info, limit: int = 10) -> List[Event]:
        # Create instances of Badge, Tag, Owner, and Service
        events_lst = fetch_events_list(limit)
        return events_lst[:limit]

    @strawberry.field
    def owners(self, info, limit: int = 1) -> List[Owner]:
        # Create instances of Owner
        owners_lst = fetch_owners_list(limit)
        return owners_lst[:limit]

    @strawberry.field
    def repositories(self, info, limit: int = 1) -> List[Repository]:
        # Create instances of Repository
        repositories_lst = fetch_repository_list(limit)
        return repositories_lst[:limit]

    @strawberry.field
    def schemas(self, info, limit: int = 1) -> List[Schema]:
        # Create instances of Schema
        schemas_lst = fetch_schema_list(limit)
        return schemas_lst[:limit]

    @strawberry.field
    def services(self, info, limit: int = 1) -> List[Service]:
        # Create instances of Service
        services_lst = fetch_services_list(limit)
        return services_lst[:limit]

    @strawberry.field
    def tags(self, info, limit: int = 1) -> List[Tag]:
        # Create instances of Tag
        tags_lst = fetch_tags_list(limit)
        return tags_lst[:limit]

    @strawberry.field
    def users(self, info, limit: int = 1) -> List[User]:
        # Create instances of User
        users_lst = fetch_users_list(limit)
        return users_lst[:limit]


schema_handler = strawberry.Schema(Query)
