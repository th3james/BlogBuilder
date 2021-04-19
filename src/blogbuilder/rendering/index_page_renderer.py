from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post_repository import RecentPostProvider
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class IndexPageRenderer:
    base_template: Template

    def render(self, recent_post_repo: RecentPostProvider) -> RenderedBlogFile:
        recent_posts = recent_post_repo.recent_posts()
        content = ""
        for post in recent_posts:
            rendered_body = MarkdownRenderer().render(post.body)

            content += f"""
                {post.slug}
                {rendered_body}
            """.format()

        content = self.base_template.render({"body": content})

        return RenderedBlogFile(Path("index.html"), content)
