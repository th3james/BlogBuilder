from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from blogbuilder.post import Post
from blogbuilder.post_file_loader import PostFileLoader


@dataclass
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
