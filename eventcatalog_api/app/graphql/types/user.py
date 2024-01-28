import random
import string
from typing import List, Optional

import strawberry


@strawberry.type
class User:
    id: str
    name: str
    role: str
    summary: Optional[str] = None
    avatarUrl: Optional[str] = None


def generate_random_user() -> User:
    # Test function to generate random user

    id = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    name = "".join(random.choices(string.ascii_letters, k=10))
    role = random.choice(["admin", "user"])
    summary = "".join(random.choices(string.ascii_letters + string.digits, k=20))
    avatarUrl = f"https://example.com/{id}/avatar"

    return User(id=id, name=name, role=role, summary=summary, avatarUrl=avatarUrl)
