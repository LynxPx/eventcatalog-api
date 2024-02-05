import json

from neomodel import ArrayProperty, JSONProperty, StringProperty, StructuredNode


class Repository(StructuredNode):
    url = StringProperty(required=True)
    # Assuming we opt for storing languages as a JSON string to accommodate both single and multiple values
    language = StringProperty(required=True)

    @property
    def language_list(self):
        # Helper property to access the language as a Python list
        return json.loads(self.language)

    @language_list.setter
    def language_list(self, value):
        # Allows setting the language property as a list, which is then stored as a JSON string
        if isinstance(value, list) or isinstance(value, str):
            self.language = json.dumps(value if isinstance(value, list) else [value])
        else:
            raise ValueError("Language must be a list or a string.")

    @classmethod
    def create(cls, url, language):
        # Create a new Repository instance
        repository = cls(url=url, language=language)
        repository.save()
        return repository

    def update(self, url=None, language=None):
        # Update the Repository instance
        if url is not None:
            self.url = url
        if language is not None:
            self.language = language
        self.save()
