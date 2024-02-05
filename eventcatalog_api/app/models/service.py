from neomodel import (
    BooleanProperty,
    RelationshipFrom,
    RelationshipTo,
    StringProperty,
    StructuredNode,
    ZeroOrMore,
)


class Service(StructuredNode):
    name = StringProperty(required=True)
    version = StringProperty(required=True)
    summary = StringProperty()
    draft = BooleanProperty()

    # Relationships
    repository = RelationshipTo(
        "Repository", "HAS_REPOSITORY", cardinality=ZeroOrMore
    )  # Assuming 0 or 1 relationship
    domain = RelationshipTo(
        "Domain", "PART_OF", cardinality=ZeroOrMore
    )  # Assuming 0 or 1 relationship
    publishes = RelationshipTo("Event", "PUBLISHES")
    subscribes = RelationshipTo("Event", "SUBSCRIBES")
    tags = RelationshipTo("Tag", "HAS_TAG")
    externalLinks = RelationshipTo(
        "Tag", "HAS_EXTERNAL_LINK"
    )  # You may need to adjust this based on your actual model
    badges = RelationshipTo("Badge", "HAS_BADGE")
    owners = RelationshipTo("Owner", "HAS_OWNER")

    # Optional properties like openAPISpec and asyncAPISpec can be added as StringProperty if needed
    openAPISpec = StringProperty()
    asyncAPISpec = StringProperty()

    @classmethod
    def create(
        cls,
        name,
        version,
        summary=None,
        draft=False,
        openAPISpec=None,
        asyncAPISpec=None,
    ):
        service = cls(
            name=name,
            version=version,
            summary=summary,
            draft=draft,
            openAPISpec=openAPISpec,
            asyncAPISpec=asyncAPISpec,
        )
        service.save()
        return service

    def update(
        self,
        name=None,
        version=None,
        summary=None,
        draft=None,
        openAPISpec=None,
        asyncAPISpec=None,
    ):
        if name:
            self.name = name
        if version:
            self.version = version
        if summary:
            self.summary = summary
        if draft is not None:
            self.draft = draft
        if openAPISpec:
            self.openAPISpec = openAPISpec
        if asyncAPISpec:
            self.asyncAPISpec = asyncAPISpec
        self.save()
