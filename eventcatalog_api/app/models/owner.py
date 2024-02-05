from neomodel import StringProperty, StructuredNode


class Owner(StructuredNode):
    id = StringProperty(unique_index=True, required=True)  # type: ignore

    # Define any relationships here if Owners relate to other entities in your graph
    # For example, a relationship to assets they own or projects they're part of
    # assets_owned = RelationshipTo('Asset', 'OWNS')
    @classmethod
    def create(cls, id):
        owner = cls(id=id)
        owner.save()
        return owner

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
