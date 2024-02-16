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
    domain_name = random.choice(
        DOMAIN_WORDS
    )  # + "-" + "".join(random.choices(string.digits, k=3))

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
            badges=get_random_badge_list(1),
        ),
        # generate_domain(),
        publishes=get_random_events_list(1),
        subscribes=get_random_events_list(2),
        tags=get_random_tags_list(3),
        externalLinks=get_random_tags_list(2),
        openAPISpec="https://example.com/openapi",
        asyncAPISpec="https://example.com/asyncapi",
        badges=get_random_badge_list(1),
        owners=get_random_owners_list(2),
    )
    return service


@strawberry.type
class Event:
    id: str
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
    story: Optional[str] = None
    alert: Optional[str] = None
    sampleTrigger: Optional[Schema] = None


def generate_random_event() -> Event:
    descriptions = [
        "A captivating event that will leave you inspired.",
        "An exciting gathering of industry experts and enthusiasts.",
        "Join us for an informative session filled with valuable insights.",
        "Experience a unique event that combines education and entertainment.",
        "Discover the latest trends and innovations in this engaging event.",
    ]

    event = Event(
        id="random-id",
        name="Random Event",
        version="1.0",
        draft=random.choice([True, False]),
        summary=random.choice(descriptions),
        domain="Random domain",
        producerNames=["ServiceA", "ServiceB"],
        consumerNames=["ServiceX", "ServiceY"],
        # producers= generate_random_service(),
        # consumers=generate_random_service(),
        badges=get_random_badge_list(1),
        tags=get_random_tags_list(2),
        openAPISpec="Random OpenAPI spec",
        historicVersions=["1.0", "2.0"],
        owners=get_random_owners_list(2),
        examples="Random examples",
        schema=generate_random_schema(),
        externalLinks=get_random_tags_list(1),
        story="Random event lengthy story",
        alert="Random event alert",
        sampleTrigger=generate_random_schema(),
    )
    return event


def get_random_events_list(limit: int) -> List[Event]:
    return [generate_random_event() for _ in range(limit)]


def get_controlled_events_list(limit: int) -> List[Event]:
    return [generate_random_event() for _ in range(limit)]


def generate_event_name() -> str:
    words = [
        ("8067545f-0099-4c1a-9bc5-59c421295f37", "Market"),
        ("aee350b4-fdec-4d8c-85a4-766209c6f59a", "Shop"),
        ("61faf0c9-1ab8-4596-a2f0-9fea80f9876b", "Stream"),
        ("800d5a2e-0841-45a9-9d4b-4382eaf989eb", "Data"),
        ("cf235599-d9a4-4908-ade0-1dd70320c5d9", "Files"),
        ("a1edc515-303f-426f-b67b-0e87fd2e99be", "Recipes"),
        ("9f984574-7831-474f-8d5f-a8023f4d8160", "Analytics"),
        ("c0d06924-28ef-4e3e-b803-c409a39c81a5", "Cars"),
    ]
    # return random.choice(words) + "-" + "".join(random.choices(string.digits, k=3))
    return random.choice(words)


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
    domain_names = [
        "Intake",
        "Compliance",
        "Case Management",
        "Account Management",
        "Taxpayer Experience",
        "Internal Operations",
    ]

    domain_name = random.choice(domain_names)

    return Domain(
        name=domain_name,
        summary="Summary for {}".format(domain_name),
        services=generate_random_service(),
        events=get_random_events_list(3),
        owners=get_random_owners_list(2),
        tags=get_random_tags_list(2),
        externalLinks=[get_random_tags_list(2)],
        badges=get_random_badge_list(1),
    )


def generate_controlled_domains() -> List[Domain]:
    return [
        Domain(
            name="Intake",
            summary="Summary for {}".format("Intake"),
            services=generate_random_service(),
            events=get_random_events_list(3),
            owners=get_random_owners_list(2),
            tags=get_random_tags_list(2),
            externalLinks=[get_random_tags_list(2)],
            badges=get_random_badge_list(1),
        ),
        Domain(
            name="Compliance",
            summary="Summary for {}".format("Compliance"),
            services=generate_random_service(),
            events=get_random_events_list(3),
            owners=get_random_owners_list(2),
            tags=get_random_tags_list(2),
            externalLinks=[get_random_tags_list(2)],
            badges=get_random_badge_list(1),
        ),
        Domain(
            name="Case Management",
            summary="Summary for {}".format("Case Management"),
            services=generate_random_service(),
            events=get_random_events_list(3),
            owners=get_random_owners_list(2),
            tags=get_random_tags_list(2),
            externalLinks=[get_random_tags_list(2)],
            badges=get_random_badge_list(1),
        ),
        Domain(
            name="Account Management",
            summary="Summary for {}".format("Account Management"),
            services=generate_random_service(),
            events=get_random_events_list(3),
            owners=get_random_owners_list(2),
            tags=get_random_tags_list(2),
            externalLinks=[get_random_tags_list(2)],
            badges=get_random_badge_list(1),
        ),
        Domain(
            name="Taxpayer Experience",
            summary="Summary for {}".format("Taxpayer Experience"),
            services=generate_random_service(),
            events=get_random_events_list(3),
            owners=get_random_owners_list(2),
            tags=get_random_tags_list(2),
            externalLinks=[get_random_tags_list(2)],
            badges=get_random_badge_list(1),
        ),
        # Domain(
        #     name="Internal Operations",
        #     summary="Summary for {}".format("Internal Operations"),
        #     services=generate_random_service(),
        #     events=get_random_events_list(3),
        #     owners=get_random_owners_list(2),
        #     tags=get_random_tags_list(2),
        #     externalLinks=[get_random_tags_list(2)],
        #     badges=get_random_badge_list(1),
        # ),
    ]
