from enum import Enum

import strawberry


@strawberry.enum
class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    WHITE = "white"
    BLACK = "black"
