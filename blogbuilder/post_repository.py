from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from blogbuilder.post import Post


@dataclass
class PostRepository:
    data_dir: Path

    def get_all(self) -> Iterable[Post]:
        input_file_paths = [f for f in self.data_dir.glob("*") if f.is_file()]
        output_file_paths: List[Path] = []
        for input_file_path in input_file_paths:
            chrooted_path = input_file_path.relative_to(self.data_dir)
            parent_dir = chrooted_path.parents[0]
            post_name = chrooted_path.stem
            output_file_path = parent_dir / Path(f"{post_name}.html")
            output_file_paths.append(output_file_path)

        return [Post(p) for p in output_file_paths]
