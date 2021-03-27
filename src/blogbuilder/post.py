from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    slug: str
    body: str
