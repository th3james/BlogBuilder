from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    body: str
    timestamp: "datetime"

    @property
    def url_path(self) -> str:
        return f"/post/{self.slug}.html"

    @property
    def file_path(self) -> Path:
        return Path(f".{self.url_path}")
