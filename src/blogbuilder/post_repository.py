from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Protocol, Tuple

from blogbuilder.post import Post
from blogbuilder.post_file_loader import PostFileLoader


class RecentPostProvider(Protocol):
    def recent_posts(self) -> Iterable[Post]:
        ...


class Month:
    @property
    def name(self) -> str:
        pass


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
        pass
