from neomodel import RelationshipFrom, RelationshipTo, StringProperty, StructuredNode

from eventcatalog_api.app.models.badge import Badge
from eventcatalog_api.app.models.event import Event
from eventcatalog_api.app.models.owner import Owner
from eventcatalog_api.app.models.service import Service
from eventcatalog_api.app.models.tag import Tag


class Domain(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    summary = StringProperty(required=True)

    # Relationships
    services = RelationshipFrom("Service", "BELONGS_TO")
    events = RelationshipFrom("Event", "ASSOCIATED_WITH")
    owners = RelationshipTo("Owner", "OWNED_BY")
    tags = RelationshipTo("Tag", "HAS_TAG")
    externalLinks = RelationshipTo(
        "Tag", "HAS_EXTERNAL_LINK"
    )  # Assuming the use of Tag for external links
    badges = RelationshipTo("Badge", "HAS_BADGE")

    # Notice that for relationships, we use RelationshipTo for outgoing relationships
    # and RelationshipFrom for incoming relationships, depending on the direction
    # of the relationship you want to model in your Neo4j graph.
    @classmethod
    def create(cls, name, summary):
        domain = cls(name=name, summary=summary)
        domain.save()
        return domain

    def add_service_to_domain(self, domain_name, service_id):
        domain = Domain.nodes.get(name=domain_name)
        service = Service.nodes.get(id=service_id)
        domain.services.connect(service)

    def associate_event_with_domain(self, domain_name, event_id):
        domain = Domain.nodes.get(name=domain_name)
        event = Event.nodes.get(id=event_id)
        domain.events.connect(event)

    def add_owner_to_domain(self, domain_name, owner_id):
        domain = Domain.nodes.get(name=domain_name)
        owner = Owner.nodes.get(id=owner_id)
        domain.owners.connect(owner)

    def tag_domain(self, domain_name, tag_id):
        domain = Domain.nodes.get(name=domain_name)
        tag = Tag.nodes.get(id=tag_id)
        domain.tags.connect(tag)

    def add_badge_to_domain(self, domain_name, badge_id):
        domain = Domain.nodes.get(name=domain_name)
        badge = Badge.nodes.get(id=badge_id)
        domain.badges.connect(badge)

    def add_external_link_to_domain(self, domain_name, tag_id):
        domain = Domain.nodes.get(name=domain_name)
        tag = Tag.nodes.get(id=tag_id)
        domain.externalLinks.connect(tag)
