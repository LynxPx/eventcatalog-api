from neomodel import StringProperty, StructuredNode


class Tag(StructuredNode):
    label = StringProperty(unique_index=True, required=True)
    url = StringProperty()
