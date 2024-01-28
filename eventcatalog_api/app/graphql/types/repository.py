import random
from typing import List, Union

import strawberry


@strawberry.type
class Repository:
    url: str
    language: str or list[str]


def generate_random_repo(limit: int) -> Repository:
    urls = [
        "https://github.com/example1",
        "https://github.com/example2",
        "https://github.com/example3",
    ]
    languages = ["Python", "Java", "JavaScript", "C++"]

    repos = []
    for i in range(limit):
        url = urls[0]  # random.choices(urls, k=1)[0]
        language = languages[1]  # random.choices(languages, k=1)[0]
        repos.append(Repository(url=url, language=language))

    return repos


def get_random_repository_list(limit: int) -> List[Repository]:
    # return [generate_random_repo() for _ in range(limit)]
    return generate_random_repo(limit)
