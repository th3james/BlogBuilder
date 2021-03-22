from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post import Post
from blogbuilder.templates.template import Template
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer


@dataclass(frozen=True)
class PostRenderer:
    base_template: Template

    def render(self, post: Post) -> RenderedBlogFile:
        body_html = MarkdownRenderer().render(post.body)
        content = self.base_template.render({"body": body_html})
        return RenderedBlogFile(Path(post.slug + ".html"), content)
