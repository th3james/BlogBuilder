from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Protocol, Tuple

from blogbuilder.post import Post
from blogbuilder.post_file_loader import PostFileLoader


class RecentPostProvider(Protocol):
    def recent_posts(self) -> Iterable[Post]:
        ...


@dataclass(frozen=True)
class Month:
    datetime: datetime

    @classmethod
    def from_datetime(cls, datetime: datetime) -> "Month":
        month_int = datetime.month
        if month_int < 10:
            month_str = f"0{month_int}"
        else:
            month_str = f"{month_int}"
        return Month(datetime.fromisoformat(f"{datetime.year}-{month_str}-01"))

    @property
    def name(self) -> str:
        return self.datetime.strftime("%B %Y")


PostArchive = Iterable[Tuple[Month, Iterable[Post]]]


@dataclass(frozen=True)
class PostRepository:
    posts: Iterable[Post]

    @classmethod
    def load_from_directory(cls, data_dir: Path) -> "PostRepository":
        input_file_paths = [f for f in data_dir.glob("*.md") if f.is_file()]
        post_file_loader = PostFileLoader(data_dir)
        posts: List[Post] = []
        for input_file_path in input_file_paths:
            posts.append(post_file_loader.load(input_file_path))

        return cls(posts)

    def recent_posts(self) -> Iterable[Post]:
        return sorted(self.posts, key=lambda p: p.timestamp, reverse=True)[:5]

    def archive(self) -> PostArchive:
        collection: dict[Month, list[Post]] = defaultdict(list)
        for p in self.posts:
            month = Month.from_datetime(p.timestamp)
            collection[month] = collection[month] + [p]

        return [(m, collection[m]) for m in collection.keys()]
