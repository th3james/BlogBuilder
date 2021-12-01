from pathlib import Path

from blogbuilder.blog_data_reader import BlogDataReader
from blogbuilder.output_writer import OutputWriter
from blogbuilder.rendering.blog_renderer import BlogRenderer


class BlogBuilder:
    def build(self, input_dir: Path, output_dir: Path) -> None:
        blog_data_reader = BlogDataReader.load_from_directory(input_dir)

        output_writer = OutputWriter(output_dir)

        for x in BlogRenderer(blog_data_reader).render_all():
            output_writer.write(x)
