import random
from typing import List

from eventcatalog_api.app.graphql.types.badge import Badge, get_random_badge_list
from eventcatalog_api.app.graphql.types.main import (
    Domain,
    Event,
    Service,
    generate_domain,
    generate_event_name,
    generate_random_service,
    get_random_events_list,
)
from eventcatalog_api.app.graphql.types.owner import Owner, get_random_owners_list
from eventcatalog_api.app.graphql.types.repository import (
    Repository,
    generate_random_repo,
    get_random_repository_list,
)
from eventcatalog_api.app.graphql.types.schema import Schema, generate_random_schema
from eventcatalog_api.app.graphql.types.tag import Tag, get_random_tags_list
from eventcatalog_api.app.graphql.types.user import User, generate_random_user

DEFAULT_GENERATED_ITEMS_LIMIT = 10

# Global variables
BADGES = get_random_badge_list(DEFAULT_GENERATED_ITEMS_LIMIT)
TAGS = get_random_tags_list(DEFAULT_GENERATED_ITEMS_LIMIT)
OWNERS = get_random_owners_list(2)
PRODUCERS = [generate_random_service()]
CONSUMERS = [generate_random_service()]
VERSIONS = ["1.0", "2.0"]
SAMPLE_SCHEMA = [generate_random_schema()]
EVENTS = get_random_events_list(DEFAULT_GENERATED_ITEMS_LIMIT)
REPOSITORIES = get_random_repository_list(DEFAULT_GENERATED_ITEMS_LIMIT)


def fetch_badges_list(limit: int = 1) -> List[Badge]:
    # Generate badge objects using random generators or any other logic
    return BADGES[:limit]


def fetch_domains_list(limit: int = 1) -> List[Domain]:
    # Generate domain objects using random generators or any other logic
    domains = []
    for i in range(0, limit):
        domains.append(generate_domain())

    return domains


def fetch_events_list(limit: int = 1) -> List[Event]:
    # Create instances of Event using previously created objects
    events = []
    for i in range(0, limit):
        event = Event(
            name=generate_event_name(),
            version="1.0",
            draft=random.choice([True, False]),
            summary="Random event summary",
            domain=generate_domain().name,
            producerNames=["Producer 1", "Producer 2"],
            consumerNames=["Consumer 1", "Consumer 2"],
            producers=[
                Service(
                    name="Producer Service1",
                    summary="Random summary",
                    version=VERSIONS[0],
                ),
                Service(
                    name="Producer 2", summary="Random summary", version=VERSIONS[0]
                ),
            ],
            consumers=[
                Service(
                    name="Consumer Service1",
                    summary="Random summary",
                    version=VERSIONS[0],
                ),
                Service(
                    name="Consumer 2", summary="Random summary", version=VERSIONS[0]
                ),
            ],
            badges=get_random_badge_list(2),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
        )
        events.append(event)

    return events


def fetch_owners_list(limit: int = 1) -> List[Owner]:
    # Generate owner objects using random generators or any other logic
    return OWNERS[:limit]


def fetch_domains_list(limit: int = 1) -> List[Domain]:
    # Generate domain objects using random generators or any other logic
    return [generate_domain() for _ in range(limit)]


def fetch_repository_list(limit: int = 1) -> List[Repository]:
    # Generate repository objects using random generators or any other logic
    return REPOSITORIES[:limit]


def fetch_schema_list(limit: int = 1) -> List[Schema]:
    # Generate schema objects using random generators or any other logic
    return SAMPLE_SCHEMA[:limit]


def fetch_services_list(limit: int = 1) -> List[Service]:
    # Generate service objects using random generators or any other logic
    services = []

    for i in range(0, limit):
        service = Service(
            name="Random Service",
            version="1.0.0",
            summary="This is a random service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=generate_domain(),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        )
        services.append(service)

    return services


def fetch_users_list(limit: int = 1) -> List[User]:
    # Generate user objects using random generators or any other logic
    return [generate_random_user() for _ in range(limit)]


def fetch_tags_list(limit: int = 1) -> List[Tag]:
    # Generate tag objects using random generators or any other logic
    return TAGS[:limit]
