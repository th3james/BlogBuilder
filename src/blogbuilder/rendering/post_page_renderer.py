from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post import Post
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class PostPageRenderer:
    base_template: Template
    blog_name: str

    def render(self, post: Post) -> RenderedBlogFile:
        post_html = PostRenderer().render(post)
        page_title = f"{self.blog_name} | {post.title}"
        content = self.base_template.render(
            {"blog_name": self.blog_name, "page_title": page_title, "body": post_html}
        )
        return RenderedBlogFile(Path(post.file_path), content)
