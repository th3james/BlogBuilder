from pathlib import Path

from blogbuilder.post_repository import PostRepository
from blogbuilder.templates.template_repository import TemplateRepository
from blogbuilder.rendering.blog_renderer import BlogRenderer
from blogbuilder.output_writer import OutputWriter


class BlogBuilder:
    def build(
        self, blog_name: str, data_dir: Path, templates_dir: Path, output_dir: Path
    ) -> None:
        post_repository = PostRepository.load_from_directory(data_dir)
        templates_repository = TemplateRepository.load_from_directory(templates_dir)

        output_writer = OutputWriter(output_dir)

        for x in BlogRenderer(
            blog_name, post_repository, templates_repository
        ).render_all():
            output_writer.write(x)
