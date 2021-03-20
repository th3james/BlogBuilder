from dataclasses import dataclass
from pathlib import Path

from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile


@dataclass
class OutputWriter:
    output_dir: Path

    def write(self, blog_file: RenderedBlogFile) -> None:
        output_path = self.output_dir / blog_file.path
        output_path.parents[0].mkdir(parents=True, exist_ok=True)
        output_path.write_text(blog_file.content)
