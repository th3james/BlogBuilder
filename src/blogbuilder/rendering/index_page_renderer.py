from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post_repository import RecentPostProvider
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class IndexPageRenderer:
    base_template: Template
    blog_name: str

    def render(self, recent_post_repo: RecentPostProvider) -> RenderedBlogFile:
        recent_posts = recent_post_repo.recent_posts()
        content = ""

        for post in recent_posts:
            content += PostRenderer().render(post)

        content = self.base_template.render(
            {"page_title": self.blog_name, "blog_name": self.blog_name, "body": content}
        )

        return RenderedBlogFile(Path("index.html"), content)
