from pathlib import Path
from typing import Iterable

from blogbuilder.post import Post


class PostRepository:
    def __init__(self, data_dir: Path) -> None:
        pass

    def get_all(self) -> Iterable[Post]:
        return []
