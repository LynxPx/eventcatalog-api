import random
from typing import List

from eventcatalog_api.app.graphql.types.badge import Badge, get_random_badge_list
from eventcatalog_api.app.graphql.types.main import (
    Domain,
    Event,
    Service,
    generate_controlled_domains,
    generate_domain,
    generate_event_name,
    generate_random_service,
    generate_service_name,
    get_random_events_list,
)
from eventcatalog_api.app.graphql.types.owner import Owner, get_random_owners_list
from eventcatalog_api.app.graphql.types.repository import (
    Repository,
    generate_random_repo,
    get_random_repository_list,
)
from eventcatalog_api.app.graphql.types.schema import (
    Schema,
    generate_random_schema,
    generate_random_trigger_schema,
)
from eventcatalog_api.app.graphql.types.tag import Tag, get_random_tags_list
from eventcatalog_api.app.graphql.types.user import User, generate_random_user
from eventcatalog_api.app.utils.color import Color

DEFAULT_GENERATED_ITEMS_LIMIT = 10

# Global variables
BADGES = get_random_badge_list(DEFAULT_GENERATED_ITEMS_LIMIT)
TAGS = get_random_tags_list(DEFAULT_GENERATED_ITEMS_LIMIT)
OWNERS = get_random_owners_list(2)
PRODUCERS = [generate_random_service()]
CONSUMERS = [generate_random_service()]
VERSIONS = ["v0.1.0", "v0.1.2", "v1.0"]
SAMPLE_SCHEMA = [generate_random_schema()]
EVENTS = get_random_events_list(DEFAULT_GENERATED_ITEMS_LIMIT)
REPOSITORIES = get_random_repository_list(DEFAULT_GENERATED_ITEMS_LIMIT)


def fetch_badges_list(limit: int = 1) -> List[Badge]:
    # Generate badge objects using random generators or any other logic
    return BADGES[:limit]


def fetch_domains_list(limit: int = 1, controlled: bool = False) -> List[Domain]:
    # Generate domain objects using random generators or any other logic
    if controlled:
        return generate_controlled_domains()

    domains = []
    for i in range(0, limit):
        domains.append(generate_domain())

    return domains


def fetch_events_list(limit: int = 10) -> List[Event]:
    # Create instances of Event using previously created objects
    descriptions = [
        "Leverage Kafka events to streamline your business processes and drive real-time decision making.",
        "Optimize your business operations with Kafka events, enabling seamless data integration and actionable insights.",
        "Unlock the power of event-driven architecture with Kafka events to enhance customer experiences and gain a competitive edge.",
        "Discover the potential of Kafka events for data-driven innovation and strategic business growth.",
        "Join industry experts to explore the transformative impact of Kafka events on business efficiency and agility.",
    ]

    events = []
    for i in range(0, limit):
        event_r = generate_event_name()
        event_id = event_r[0]
        event_name = event_r[1]

        event = Event(
            id=event_id,
            name=event_name,
            version=random.choice(VERSIONS),
            draft=random.choice([True, False]),
            summary=random.choice(descriptions),
            domain=generate_domain().name,
            producerNames=["ServiceA", "ServiceB"],
            consumerNames=["ServiceX", "ServiceY"],
            producers=[
                Service(
                    name="Submission Initiator",
                    id="8067545f-0099-4c1a-9bc5-11c421295f31",
                    summary="Submission Initiator",
                    version=random.choice(VERSIONS),
                ),
                Service(
                    name="Compliance",
                    id="aee350b4-fdec-4d8c-85a4-126209c6f592",
                    summary="Compliance",
                    version=random.choice(VERSIONS),
                ),
            ],
            consumers=[
                Service(
                    name="1040 Validator",
                    id="61faf0c9-1ab8-4596-a2f0-13ea80f98763",
                    summary="1040 Validator",
                    version=random.choice(VERSIONS),
                ),
                Service(
                    name="ARS Event(Automated Resolution System)",
                    id="800d5a2e-0841-45a9-9d4b-1482eaf989e4",
                    summary="ARS Event(Automated Resolution System)",
                    version=random.choice(VERSIONS),
                ),
            ],
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
            story="""This event can be triggered multiple times per customer. Everytime the customer adds an item to their shopping cart this event will be triggered.

We have a frontend application that allows users to buy things from our store. This front end interacts directly with the Basket Service to add items to the cart. The Basket Service will raise the events.""",
        )
        events.append(event)

    return events


def fetch_controlled_events_list(id: str = "") -> List[Event]:
    events = [
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f01",
            name="Transmission.SubmissionReceived",
            domain="Intake",
            summary="Confirms receipt of an e-filed 1040 submission.",
            story="The `SubmissionReceived` event relates to a Form 1040 that is received by the Submission Initiator. The Submission Initiator will trigger the `SubmissionReceived` event.",
            producerNames=["Submission Initiator"],
            consumerNames=[
                "Compliance",
                "1040 Validator",
                "ARS Event(Automated Resolution System)",
            ],
            producers=[
                Service(
                    name="Submission Initiator",
                    id="8067545f-0099-4c1a-9bc5-11c421295f31",
                    summary="Submission Initiator",
                    version=random.choice(VERSIONS),
                )
            ],
            consumers=[
                Service(
                    name="Compliance",
                    id="aee350b4-fdec-4d8c-85a4-126209c6f592",
                    summary="Compliance",
                    version=random.choice(VERSIONS),
                ),
                Service(
                    name="1040 Validator",
                    id="61faf0c9-1ab8-4596-a2f0-13ea80f98763",
                    summary="1040 Validator",
                    version=random.choice(VERSIONS),
                ),
                Service(
                    name="ARS Event(Automated Resolution System)",
                    id="800d5a2e-0841-45a9-9d4b-1482eaf989e4",
                    summary="ARS Event(Automated Resolution System)y",
                    version=random.choice(VERSIONS),
                ),
            ],
            draft=False,
            version="v0.0.1",
            badges=[
                Badge(
                    content="New",
                    backgroundColor=Color.BLUE.value,
                    textColor=Color.BLUE.value,
                )
            ],
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f0122",
            name="Transmission.ResponseReceived",
            domain="Intake",
            summary="Confirms that the e-filed 1040 has been processed through the Validation Service.",
            story="The `ResponseReceived` event confirms that the Form 1040 that was submitted has processed through the Validation Resolution Service. The Validation Resolution Service is responsible for triggering the `ResponseReceived` event.",
            producerNames=["Validation Resolution Service"],
            consumerNames=["Submission Completer", "Notification Service"],
            producers=[
                Service(
                    name="Validation Resolution Service",
                    id="cf235599-d9a4-4908-ade0-15d70320c5d5",
                    summary="Validation Resolution Service",
                    version=random.choice(VERSIONS),
                )
            ],
            consumers=[
                Service(
                    name="Submission Completer",
                    id="a1edc515-303f-426f-b67b-1687fd2e99b6",
                    summary="Submission Completer",
                    version=random.choice(VERSIONS),
                ),
                Service(
                    name="Notification Service",
                    id="9f984574-7831-474f-8d5f-17023f4d8167",
                    summary="Notification Service",
                    version=random.choice(VERSIONS),
                ),
            ],
            draft=False,
            version="v0.0.1",
            badges=[
                Badge(
                    content="New",
                    backgroundColor=Color.BLUE.value,
                    textColor=Color.BLUE.value,
                )
            ],
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f0133",
            name="Transmission.AcceptanceReceived",
            domain="Intake",
            summary="Confirms acceptance of an e-filed 1040 submission.",
            story="The `AcceptanceReceived` event relates to a Form 1040 that has been fully accepted with no issues identified.",
            producerNames=["Validation Resolution Service"],
            producers=[
                Service(
                    name="Validation Resolution Service",
                    id="cf235599-d9a4-4908-ade0-15d70320c5d5",
                    summary="Validation Resolution Service",
                    version=random.choice(VERSIONS),
                )
            ],
            draft=False,
            version="v0.0.1",
            badges=[
                Badge(
                    content="New",
                    backgroundColor=Color.BLUE.value,
                    textColor=Color.BLUE.value,
                )
            ],
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f0144",
            name="Transmission.ErrorNotResolved",
            domain="Intake",
            summary="Confirms e-filed 1040 errors could not be auto corrected.",
            story="The `ErrorNotResolved` identifies that the submitted Form 1040 errors were not able to be automatically corrected and will require additional information from the taxpayer.",
            producerNames=["ARS Event(Automated Resolution System)"],
            producers=[
                Service(
                    name="ARS Event(Automated Resolution System)",
                    id="800d5a2e-0841-45a9-9d4b-1482eaf989e4",
                    summary="ARS Event(Automated Resolution System)",
                    version=random.choice(VERSIONS),
                )
            ],
            draft=False,
            version="v0.0.1",
            badges=[
                Badge(
                    content="New",
                    backgroundColor=Color.BLUE.value,
                    textColor=Color.BLUE.value,
                )
            ],
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f02",
            name="Transmission.FileReceived.Error",
            domain="Intake",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f03",
            name="Transmission.ProcessingCompleted",
            domain="Intake",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f04",
            name="Transmission.ProcessingCompleted.Error",
            domain="Intake",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f05",
            name="TaxTransaction.PerfectionPassed",
            domain="Intake",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f06",
            name="TaxTransaction.PerfectionPassed.Error",
            domain="Intake",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f07",
            name="TaxTransaction.AnamoliesDetected",
            domain="Compliance",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f08",
            name="TaxTransaction.AnamoliesDetected.Error",
            domain="Compliance",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f09",
            name="TaxTransaction.ComplianceIssueinInventory",
            domain="Compliance",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f10",
            name="TaxTransaction.ComplianceIssueinInventory.Error",
            domain="Compliance",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f11",
            name="Case.CaseOpened",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f12",
            name="Case.CaseOpened.Error",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f13",
            name="Correspondence.CorrespondenceRequested",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f14",
            name="Correspondence.CorrespondenceRequested.Error",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f15",
            name="Correspondence.CorrespondenceReceived",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f16",
            name="Correspondence.CorrespondenceReceived.Error",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f17",
            name="Case.CaseClosed",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f18",
            name="Case.CaseClosed.Error",
            domain="Case Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f19",
            name="Transaction.Received",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f20",
            name="Transaction.Received.Error",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f21",
            name="Transaction.Analyzed",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f23",
            name="Transaction.Analyzed.Error",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f24",
            name="Transaction.Posted",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f26",
            name="Transaction.Posted.Error",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f27",
            name="Transaction.Settled",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
        Event(
            id="8067545f-0099-4c1a-9bc5-59c421295f28",
            name="Transaction.Settled.Error",
            domain="Account Management",
            version="v0.0.1",
            draft=random.choice([True, False]),
            badges=get_random_badge_list(1),
            tags=TAGS[:2],
            openAPISpec="Random OpenAPI spec",
            historicVersions=["1.0", "2.0"],
            owners=OWNERS,
            examples="Random examples",
            schema=generate_random_schema(),
            externalLinks=TAGS[:1],
            alert="When firing this event make sure you set the `correlation-id` in the headers. Our schemas have standard metadata make sure you read and follow it.",
            sampleTrigger=generate_random_trigger_schema(),
        ),
    ]

    if id:
        for e in events:
            if e.id == id:
                return e
        return None
    return events


def fetch_owners_list(limit: int = 1) -> List[Owner]:
    # Generate owner objects using random generators or any other logic
    return OWNERS[:limit]


def fetch_domains_list(limit: int = 5, controlled: bool = False) -> List[Domain]:
    # Generate domain objects using random generators or any other logic
    if controlled:
        return generate_controlled_domains()

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
    # services_names = ["ServiceA", "ServiceB", "ServiceX", "ServiceY"]

    for i in range(0, limit):
        service_details = generate_service_name()

        service = Service(
            name=service_details[1],
            id=service_details[0],
            version=random.choice(VERSIONS),
            summary="This is a service",
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


def fetch_controlled_services_list(limit: int = 6) -> List[Service]:
    services = [
        ("8067545f-0099-4c1a-9bc5-11c421295f31", "Submission Initiator"),
        ("aee350b4-fdec-4d8c-85a4-126209c6f592", "Compliance"),
        ("61faf0c9-1ab8-4596-a2f0-13ea80f98763", "1040 Validator"),
        (
            "800d5a2e-0841-45a9-9d4b-1482eaf989e4",
            "ARS Event(Automated Resolution System)",
        ),
        ("cf235599-d9a4-4908-ade0-15d70320c5d5", "Validation Resolution Service"),
        ("a1edc515-303f-426f-b67b-1687fd2e99b6", "Submission Completer"),
        ("9f984574-7831-474f-8d5f-17023f4d8167", "Notification Service"),
        ("c0d06924-28ef-4e3e-b803-1809a39c81a8", "ServiceH"),
    ]

    return [
        Service(
            name=services[0][1],
            id=services[0][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
        Service(
            name=services[1][1],
            id=services[1][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
        Service(
            name=services[2][1],
            id=services[2][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
        Service(
            name=services[3][1],
            id=services[3][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
        Service(
            name=services[3][1],
            id=services[3][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
        Service(
            name=services[4][1],
            id=services[4][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
        Service(
            name=services[5][1],
            id=services[5][0],
            version=random.choice(VERSIONS),
            summary="This is a service",
            draft=random.choice([True, False]),
            repository=generate_random_repo(1),
            domain=random.choice(generate_controlled_domains()),
            publishes=random.sample(EVENTS, random.randint(1, 2)),
            subscribes=random.sample(EVENTS, random.randint(1, 2)),
            tags=random.sample(TAGS, random.randint(1, 3)),
            externalLinks=random.sample(TAGS, random.randint(1, 2)),
            openAPISpec="https://example.com/openapi",
            asyncAPISpec="https://example.com/asyncapi",
            badges=random.sample(BADGES, random.randint(1, 2)),
            owners=random.sample(OWNERS, random.randint(1, 2)),
        ),
    ][:limit]


def fetch_users_list(limit: int = 1) -> List[User]:
    # Generate user objects using random generators or any other logic
    return [generate_random_user() for _ in range(limit)]


def fetch_tags_list(limit: int = 1) -> List[Tag]:
    # Generate tag objects using random generators or any other logic
    return TAGS[:limit]
