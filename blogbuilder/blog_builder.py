from pathlib import Path

from blogbuilder.post_repository import PostRepository
from blogbuilder.template_repository import TemplateRepository
from blogbuilder.blog_renderer import BlogRenderer
from blogbuilder.output_writer import OutputWriter


class BlogBuilder:
    def build(self, data_dir: Path, templates_dir: Path, output_dir: Path) -> None:
        output_writer = OutputWriter()
        for x in BlogRenderer().render_all():
            output_writer.write(x)