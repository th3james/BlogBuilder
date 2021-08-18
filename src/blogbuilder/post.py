from dataclasses import dataclass


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    body: str

    @property
    def path(self) -> str:
        return f"/post/{self.slug}.html"
