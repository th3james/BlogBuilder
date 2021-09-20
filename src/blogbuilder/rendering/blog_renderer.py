from dataclasses import dataclass
from typing import Iterable, List

from blogbuilder.post_repository import PostRepository
from blogbuilder.rendering.index_page_renderer import IndexPageRenderer
from blogbuilder.rendering.post_page_renderer import PostPageRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template_repository import TemplateRepository


@dataclass(frozen=True)
class BlogRenderer:
    blog_name: str
    post_repository: PostRepository
    template_repository: TemplateRepository

    def render_all(self) -> Iterable[RenderedBlogFile]:
        index_page = IndexPageRenderer(
            self.template_repository.base_template, self.blog_name
        ).render(self.post_repository)
        files: List[RenderedBlogFile] = [index_page]
        for post in self.post_repository.posts:
            files.append(
                PostPageRenderer(
                    self.template_repository.base_template, self.blog_name
                ).render(post)
            )
        return files
