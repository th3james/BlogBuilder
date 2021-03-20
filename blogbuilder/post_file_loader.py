from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post import Post


@dataclass(frozen=True)
class PostFileLoader:
    base_input_dir: Path

    def load(self, input_file_path: Path) -> Post:
        chrooted_path = input_file_path.relative_to(self.base_input_dir)
        return Post(chrooted_path.stem, input_file_path.read_text())
