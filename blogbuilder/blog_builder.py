from pathlib import Path

from blogbuilder.post_repository import PostRepository
from blogbuilder.template_repository import TemplateRepository
from blogbuilder.blog_renderer import BlogRenderer
from blogbuilder.output_writer import OutputWriter


class BlogBuilder:
    def build(self, data_dir: Path, templates_dir: Path, output_dir: Path) -> None:
        post_repository = PostRepository(data_dir)
        templates_repository = TemplateRepository(templates_dir)

        output_writer = OutputWriter(output_dir)

        for x in BlogRenderer(post_repository, templates_repository).render_all():
            output_writer.write(x)
