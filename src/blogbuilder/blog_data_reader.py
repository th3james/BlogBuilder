from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post_repository import PostRepository
from blogbuilder.templates.template_repository import TemplateRepository


@dataclass(frozen=True)
class BlogDataReader:
    blog_name: str
    post_repository: PostRepository
    template_repository: TemplateRepository

    @classmethod
    def load_from_directory(cls, input_dir: Path) -> "BlogDataReader":
        blog_name = (input_dir / "blog_name.txt").read_text().strip()
        post_repository = PostRepository.load_from_directory(input_dir / "posts")
        template_repository = TemplateRepository.load_from_directory(
            input_dir / "templates"
        )

        return cls(blog_name, post_repository, template_repository)
