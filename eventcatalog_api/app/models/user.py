from neomodel import StringProperty, StructuredNode, UniqueIdProperty


class User(StructuredNode):
    id = UniqueIdProperty()  # type: ignore
    name = StringProperty(required=True)
    role = StringProperty(required=True)
    summary = StringProperty()
    avatarUrl = StringProperty()

    def create(self):
        """
        Create a new user node in the graph.
        """
        self.save()

    def update(self, **kwargs):
        """
        Update the user node with the provided attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    # Define any relationships here if Users relate to other entities in your graph
    # For example, a relationship to posts or comments if it's a social media app
    # posts = RelationshipTo('Post', 'HAS_POSTED')
