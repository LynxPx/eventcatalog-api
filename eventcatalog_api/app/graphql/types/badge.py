import random
import string
from typing import List

import strawberry

from eventcatalog_api.app.utils.color import Color


@strawberry.type
class Badge:
    content: str
    backgroundColor: str
    textColor: str


def generate_random_badge() -> Badge:
    badge_content = ["New", "Recently Updated", "Deprecated", "Draft"]
    content = random.choice(badge_content)

    backgroundColor = random.choice(
        [
            Color.BLACK.value,
            Color.WHITE.value,
            Color.RED.value,
            Color.BLUE.value,
            Color.GREEN.value,
            Color.YELLOW.value,
        ]
    )
    textColor = random.choice(
        [
            Color.BLACK.value,
            Color.WHITE.value,
            Color.RED.value,
            Color.BLUE.value,
            Color.GREEN.value,
            Color.YELLOW.value,
        ]
    )

    return Badge(content=content, backgroundColor=backgroundColor, textColor=textColor)


def get_random_badge_list(limit: int) -> List[Badge]:
    return [generate_random_badge() for _ in range(limit)]
