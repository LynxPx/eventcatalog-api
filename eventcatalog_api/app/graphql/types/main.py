import random
import string
from typing import List, Optional

import strawberry

from eventcatalog_api.app.graphql.types.badge import Badge, get_random_badge_list
from eventcatalog_api.app.graphql.types.owner import Owner, get_random_owners_list
from eventcatalog_api.app.graphql.types.repository import (
    Repository,
    generate_random_repo,
)
from eventcatalog_api.app.graphql.types.schema import Schema, generate_random_schema

# from eventcatalog_api.app.graphql.types.service import Service
from eventcatalog_api.app.graphql.types.tag import Tag, get_random_tags_list

DOMAIN_WORDS = [
    "Business",
    "IT Support",
    "Forecasting",
    "Business Inteliggence",
    "Billing",
    "Marketing",
]


@strawberry.type
class Service:
    name: str
    version: str
    summary: Optional[str] = None
    draft: Optional[bool] = None
    repository: Optional[Repository] = None
    domain: Optional["Domain"] = None  # Forward Declaration
    publishes: Optional[List["Event"]] = None  # Forward Declaration
    subscribes: Optional[List["Event"]] = None  # Forward Declaration
    tags: Optional[List[Tag]] = None
    externalLinks: Optional[List[Tag]] = None
    openAPISpec: Optional[str] = None
    asyncAPISpec: Optional[str] = None
    badges: Optional[List[Badge]] = None
    owners: Optional[List[Owner]] = None


def generate_random_service() -> Service:
    domain_name = (
        random.choice(DOMAIN_WORDS) + "-" + "".join(random.choices(string.digits, k=3))
    )

    service = Service(
        name="Random Service",
        version="1.0.0",
        summary="This is a random service",
        draft=False,  # random.choice([True, False]),
        repository=Repository(url="", language=""),  # generate_random_repo(1),
        domain=Domain(
            name=domain_name,
            summary="Summary for {}".format(domain_name),
            # services=generate_random_service(), # Nested call causes issues
            events=get_random_events_list(3),
            owners=get_random_owners_list(2),
            tags=get_random_tags_list(2),
            externalLinks=[get_random_tags_list(2)],
            badges=get_random_badge_list(2),
        ),
        # generate_domain(),
        publishes=get_random_events_list(1),
        subscribes=get_random_events_list(2),
        tags=get_random_tags_list(3),
        externalLinks=get_random_tags_list(2),
        openAPISpec="https://example.com/openapi",
        asyncAPISpec="https://example.com/asyncapi",
        badges=get_random_badge_list(2),
        owners=get_random_owners_list(2),
    )
    return service


@strawberry.type
class Event:
    name: str
    version: str
    draft: Optional[bool] = None
    summary: Optional[str] = None
    domain: Optional[str] = None
    producerNames: Optional[List[str]] = None
    consumerNames: Optional[List[str]] = None
    producers: Optional[List["Service"]] = None
    consumers: Optional[List["Service"]] = None
    badges: Optional[List[Badge]] = None
    tags: Optional[List[Tag]] = None
    openAPISpec: Optional[str] = None
    historicVersions: Optional[List[str]] = None
    owners: Optional[List[Owner]] = None
    examples: Optional[str] = None  # Any type?
    schema: Optional[Schema] = None  # Any type?
    externalLinks: Optional[List[Tag]] = None
    owners: Optional[List[Owner]] = None


def generate_random_event() -> Event:
    event = Event(
        name="Random Event",
        version="1.0",
        draft=random.choice([True, False]),
        summary="Random event summary",
        domain="Random domain",
        producerNames=["Producer 1", "Producer 2"],
        consumerNames=["Consumer 1", "Consumer 2"],
        # producers= generate_random_service(),
        # consumers=generate_random_service(),
        badges=get_random_badge_list(2),
        tags=get_random_tags_list(2),
        openAPISpec="Random OpenAPI spec",
        historicVersions=["1.0", "2.0"],
        owners=get_random_owners_list(2),
        examples="Random examples",
        schema=generate_random_schema(),
        externalLinks=get_random_tags_list(1),
    )
    return event


def get_random_events_list(limit: int) -> List[Event]:
    return [generate_random_event() for _ in range(limit)]


def generate_event_name() -> str:
    words = [
        "Market",
        "Shop",
        "Stream",
        "Data",
        "Files",
        "Recipes",
        "Analytics",
        "Cars",
    ]
    return random.choice(words) + "-" + "".join(random.choices(string.digits, k=3))


@strawberry.type
class Domain:
    name: str
    summary: str
    services: Optional[List["Service"]] = None
    events: Optional[List["Event"]] = None  # Forward Declaration
    owners: Optional[List[Owner]] = None
    tags: Optional[List[Tag]] = None
    externalLinks: Optional[List[Tag]] = None
    badges: Optional[List[Badge]] = None


def generate_domain() -> str:
    words = [
        "Business",
        "IT Support",
        "Forecasting",
        "Business Inteliggence",
        "Billing",
        "Marketing",
    ]

    domain_name = (
        random.choice(words) + "-" + "".join(random.choices(string.digits, k=3))
    )

    return Domain(
        name=domain_name,
        summary="Summary for {}".format(domain_name),
        services=generate_random_service(),
        events=get_random_events_list(3),
        owners=get_random_owners_list(2),
        tags=get_random_tags_list(2),
        externalLinks=[get_random_tags_list(2)],
        badges=get_random_badge_list(2),
    )
