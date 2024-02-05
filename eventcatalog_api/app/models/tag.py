from neomodel import StringProperty, StructuredNode


class Tag(StructuredNode):
    label = StringProperty(unique_index=True, required=True)
    url = StringProperty()

    @classmethod
    def create(cls, label, url):
        tag = cls(label=label, url=url)
        tag.save()
        return tag

    def update(self, label=None, url=None):
        if label is not None:
            self.label = label
        if url is not None:
            self.url = url
        self.save()
