from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class SchemaNode(
    StructuredNode
):  # Renamed to SchemaNode to avoid potential keyword conflicts
    id = UniqueIdProperty()  # type: ignore
    # Generates a unique identifier, use StringProperty if you want to manually set the ID
    snippet = StringProperty(required=True)
    language = StringProperty(required=True)
    extension = StringProperty()  # Optional field

    # If SchemaNode needs to relate to other entities, define those relationships here
    # For example, if schemas are associated with specific services or users:
    # related_services = RelationshipTo('Service', 'APPLIES_TO')
    @classmethod
    def create(cls, snippet, language, extension=None):
        schema_node = cls(snippet=snippet, language=language, extension=extension)
        schema_node.save()
        return schema_node

    def update(self, snippet=None, language=None, extension=None):
        if snippet is not None:
            self.snippet = snippet
        if language is not None:
            self.language = language
        if extension is not None:
            self.extension = extension
        self.save()
