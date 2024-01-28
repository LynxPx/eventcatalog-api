import random
from typing import List, Optional, Union

import strawberry


@strawberry.type
class Tag:
    label: str
    url: str


def generate_random_tag() -> Tag:
    labels = ["Tag 1", "Tag 2", "Tag 3"]
    urls = ["https://example1.com", "https://example2.com", "https://example3.com"]
    label = random.choice(labels)
    url = random.choice(urls)

    return Tag(label=label, url=url)


def get_random_tags_list(limit: int) -> List[Tag]:
    return [generate_random_tag() for _ in range(limit)]
