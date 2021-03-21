from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from blogbuilder.post_repository import PostRepository
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.template_repository import TemplateRepository


@dataclass(frozen=True)
class BlogRenderer:
    post_repository: PostRepository
    template_repository: TemplateRepository

    def render_all(self) -> Iterable[RenderedBlogFile]:
        files: List[RenderedBlogFile] = [RenderedBlogFile(Path("index.html"), "")]
        for post in self.post_repository.posts:
            files.append(
                PostRenderer(self.template_repository.base_template).render(post)
            )
        return files
