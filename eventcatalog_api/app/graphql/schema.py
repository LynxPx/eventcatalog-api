"""
schema.py  is the main GraphQL schema in a FastAPI project using Strawberry GraphQL should define the root Query, Mutation, and possibly Subscription types, which are entry points for the GraphQL API. The schema brings together all of the individual GraphQL type definitions and resolvers from different domains.
"""

import json
from typing import List, Optional

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
    fetch_controlled_events_list,
    fetch_controlled_services_list,
    fetch_domains_list,
    fetch_events_list,
    fetch_owners_list,
    fetch_repository_list,
    fetch_schema_list,
    fetch_services_list,
    fetch_tags_list,
    fetch_users_list,
)

DEFAULT_GENERATED_ITEMS_LIMIT = 100


@strawberry.type
class Query:
    @strawberry.field
    def badges(self, info, limit: int = 10) -> List[Badge]:
        # Create instances of Badge
        badges_lst = fetch_badges_list(limit)
        return badges_lst[:limit]

    @strawberry.field
    def badge(self, info, content: str) -> Optional[Badge]:
        if content:
            for e in fetch_badges_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.content == content:
                    return e

    @strawberry.field
    def domains(self, info, limit: int = 10, controlled: bool = True) -> List[Domain]:
        if controlled:
            return fetch_domains_list(limit, controlled)
        # Create instances of Domain
        domains_lst = fetch_domains_list(limit)
        return domains_lst[:limit]

    @strawberry.field
    def domain(self, info, id: str) -> Optional[Domain]:
        if id:
            for e in fetch_domains_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.id == id:
                    return e

    @strawberry.field
    def events(
        self, info, limit: int = 100, id: str = "", controlled: bool = True
    ) -> List[Event]:
        # Create instances of Badge, Tag, Owner, and Service
        if controlled:
            controlled_events = fetch_controlled_events_list()

            if id:
                for e in controlled_events:
                    if e.id == id:
                        return [e]
                return []
            return controlled_events[:limit]

        events_lst = fetch_events_list(limit)
        if id:
            for e in fetch_events_list(100):
                if e.id == id:
                    return [e]
            return []
        return events_lst[:limit]

    @strawberry.field
    def event(self, info, id: str = "", controlled: bool = True) -> Optional[Event]:
        # Create instances of Badge, Tag, Owner, and Service
        if id:
            if controlled:
                return fetch_controlled_events_list(id=id)

            for e in fetch_events_list(100):
                if e.id == id:
                    return e

    @strawberry.field
    def owners(self, info, limit: int = 10) -> List[Owner]:
        # Create instances of Owner
        owners_lst = fetch_owners_list(limit)
        return owners_lst[:limit]

    @strawberry.field
    def owner(self, info, id: str) -> Optional[Owner]:
        if id:
            for e in fetch_owners_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.id == id:
                    return e

    @strawberry.field
    def repositories(self, info, limit: int = 10) -> List[Repository]:
        # Create instances of Repository
        repositories_lst = fetch_repository_list(limit)
        return repositories_lst[:limit]

    @strawberry.field
    def repository(self, info, url: str) -> Optional[Repository]:
        if url:
            for e in fetch_repository_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.url == url:
                    return e

    @strawberry.field
    def schemas(self, info, limit: int = 10) -> List[Schema]:
        # Create instances of Schema
        schemas_lst = fetch_schema_list(limit)
        return schemas_lst[:limit]

    @strawberry.field
    def schema(self, info, id: str) -> Optional[Schema]:
        if id:
            for e in fetch_schema_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.id == id:
                    return e

    @strawberry.field
    def services(self, info, limit: int = 10, controlled: bool = True) -> List[Service]:
        # Create instances of Service
        if controlled:
            return fetch_controlled_services_list(limit)[:limit]

        services_lst = fetch_services_list(limit)
        return services_lst[:limit]

    @strawberry.field
    def service(self, info, id: str) -> Optional[Service]:
        if id:
            for e in fetch_services_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.id == id:
                    return e

    @strawberry.field
    def tags(self, info, limit: int = 10) -> List[Tag]:
        # Create instances of Tag
        tags_lst = fetch_tags_list(limit)
        return tags_lst[:limit]

    @strawberry.field
    def tag(self, info, label: str) -> Optional[Tag]:
        if label:
            for e in fetch_tags_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.label == label:
                    return e

    @strawberry.field
    def users(self, info, limit: int = 10) -> List[User]:
        # Create instances of User
        users_lst = fetch_users_list(limit)
        return users_lst[:limit]

    @strawberry.field
    def user(self, info, id: str) -> Optional[User]:
        if id:
            for e in fetch_users_list(DEFAULT_GENERATED_ITEMS_LIMIT):
                if e.id == id:
                    return e


schema_handler = strawberry.Schema(Query)
