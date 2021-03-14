from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

from blogbuilder.blog_file import BlogFile
from blogbuilder.post_repository import PostRepository
from blogbuilder.template_repository import TemplateRepository


@dataclass
class BlogRenderer:
    post_repository: PostRepository
    template_repository: TemplateRepository

    def render_all(self) -> Iterable[BlogFile]:
        files: List[BlogFile] = [BlogFile(Path("index.html"))]
        for post in self.post_repository.get_all():
            files.append(BlogFile(post.path))
        return files
