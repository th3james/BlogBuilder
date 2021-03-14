from dataclasses import dataclass
from pathlib import Path

from blogbuilder.blog_file import BlogFile


@dataclass
class OutputWriter:
    output_dir: Path

    def write(self, file: BlogFile) -> None:
        output_path = self.output_dir / file.path
        output_path.parents[0].mkdir(parents=True, exist_ok=True)
        output_path.touch()
