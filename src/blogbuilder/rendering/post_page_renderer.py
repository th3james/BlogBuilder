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
        content = self.base_template.render(
            {"body": post_html, "blog_name": self.blog_name}
        )
        return RenderedBlogFile(Path(post.file_path), content)
