from neomodel import (
    BooleanProperty,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    UniqueIdProperty,
)

from eventcatalog_api.app.models.badge import Badge
from eventcatalog_api.app.models.owner import Owner
from eventcatalog_api.app.models.service import Service
from eventcatalog_api.app.models.tag import Tag

# Assuming Badge, Tag, Owner, Service, and Schema classes are defined similar to previous instructions


class Event(StructuredNode):
    id = UniqueIdProperty()  # type: ignore
    name = StringProperty(required=True)
    version = StringProperty(required=True)
    draft = BooleanProperty()
    summary = StringProperty()
    domain = StringProperty()
    producerNames = (
        StringProperty()
    )  # This could be a list in GraphQL but needs handling in neomodel
    consumerNames = StringProperty()  # Same as above
    openAPISpec = StringProperty()
    historicVersions = StringProperty()  # Consider how to handle lists
    examples = StringProperty()  # Any type is generally represented as a string or JSON
    # For Schema, consider representing as a JSON string or defining a related node

    # Relationships
    producers = RelationshipFrom("Service", "PRODUCED_BY")
    consumers = RelationshipTo("Service", "CONSUMES")
    badges = RelationshipTo("Badge", "HAS_BADGE")
    tags = RelationshipTo("Tag", "HAS_TAG")
    externalLinks = RelationshipTo(
        "Tag", "HAS_EXTERNAL_LINK"
    )  # Assuming Tag is reused for external links
    owners = RelationshipTo("Owner", "OWNED_BY")

    # Adjust the relationship types and direction based on your specific domain model
    @classmethod
    def create(
        cls,
        name,
        version,
        draft=False,
        summary=None,
        domain=None,
        producer_names=None,
        consumer_names=None,
        openapi_spec=None,
        historic_versions=None,
        examples=None,
    ):
        event = cls(
            name=name,
            version=version,
            draft=draft,
            summary=summary,
            domain=domain,
            producerNames=producer_names,
            consumerNames=consumer_names,
            openAPISpec=openapi_spec,
            historicVersions=historic_versions,
            examples=examples,
        )
        event.save()
        return event

    def update(
        self,
        name=None,
        version=None,
        draft=None,
        summary=None,
        domain=None,
        producer_names=None,
        consumer_names=None,
        openapi_spec=None,
        historic_versions=None,
        examples=None,
    ):
        if name:
            self.name = name
        if version:
            self.version = version
        if draft is not None:
            self.draft = draft
        if summary:
            self.summary = summary
        if domain:
            self.domain = domain
        if producer_names:
            self.producerNames = producer_names
        if consumer_names:
            self.consumerNames = consumer_names
        if openapi_spec:
            self.openAPISpec = openapi_spec
        if historic_versions:
            self.historicVersions = historic_versions
        if examples:
            self.examples = examples
        self.save()

    def link_producer_to_event(self, event_id, service_id):
        event = Event.nodes.get(id=event_id)
        service = Service.nodes.get(id=service_id)
        event.producers.connect(service)

    def link_consumer_to_event(self, event_id, service_id):
        event = Event.nodes.get(id=event_id)
        service = Service.nodes.get(id=service_id)
        event.consumers.connect(service)

    def add_badge_to_event(self, event_id, badge_id):
        event = Event.nodes.get(id=event_id)
        badge = Badge.nodes.get(id=badge_id)
        event.badges.connect(badge)

    def tag_event(self, event_id, tag_id):
        event = Event.nodes.get(id=event_id)
        tag = Tag.nodes.get(id=tag_id)
        event.tags.connect(tag)

    def add_external_link_to_event(self, event_id, tag_id):
        event = Event.nodes.get(id=event_id)
        tag = Tag.nodes.get(id=tag_id)
        event.externalLinks.connect(tag)

    def link_owner_to_event(self, event_id, owner_id):
        event = Event.nodes.get(id=event_id)
        owner = Owner.nodes.get(id=owner_id)
        event.owners.connect(owner)
