from typing import Iterable
from dataclasses import dataclass

from blogbuilder.blog_file import BlogFile
from blogbuilder.post_repository import PostRepository
from blogbuilder.template_repository import TemplateRepository


@dataclass
class BlogRenderer:
    post_repository: PostRepository
    template_repository: TemplateRepository

    def render_all(self) -> Iterable[BlogFile]:
        pass
