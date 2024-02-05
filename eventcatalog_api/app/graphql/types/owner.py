import uuid
from typing import List

import strawberry


@strawberry.type
class Owner:
    id: str
    first_name: str
    last_name: str


def generate_random_owner() -> Owner:
    return Owner(id=str(uuid.uuid4()), first_name="John", last_name="Doe")


def get_random_owners_list(limit: int) -> List[Owner]:
    return [generate_random_owner() for _ in range(limit)]
