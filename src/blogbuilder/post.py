from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    body: str
