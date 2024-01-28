import random
from typing import Optional

import strawberry


@strawberry.type
class Schema:
    snippet: str
    language: str
    extension: Optional[str] = None


def generate_random_schema() -> Schema:
    snippets = ["snippet1", "snippet2", "snippet3"]  # Replace with your actual snippets
    languages = [
        "language1",
        "language2",
        "language3",
    ]  # Replace with your actual languages
    extensions = [
        "extension1",
        "extension2",
        "extension3",
    ]  # Replace with your actual extensions

    random_snippet = random.choice(snippets)
    random_language = random.choice(languages)
    random_extension = random.choice(extensions)

    return Schema(
        snippet=random_snippet, language=random_language, extension=random_extension
    )
