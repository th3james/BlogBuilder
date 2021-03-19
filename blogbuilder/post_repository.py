from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from blogbuilder.post import Post


@dataclass
class PostRepository:
    data_dir: Path

    @classmethod
    def load_from_directory(cls, data_dir: Path) -> "PostRepository":
        return cls(data_dir)

    def get_all(self) -> Iterable[Post]:
        input_file_paths = [f for f in self.data_dir.glob("*") if f.is_file()]
        posts: List[Post] = []
        for input_file_path in input_file_paths:
            chrooted_path = input_file_path.relative_to(self.data_dir)
            posts.append(Post(chrooted_path, input_file_path))

        return posts
