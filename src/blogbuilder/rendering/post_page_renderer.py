from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post import Post
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class PostPageRenderer:
    base_template: Template

    def render(self, post: Post) -> RenderedBlogFile:
        post_html = PostRenderer().render(post)
        content = self.base_template.render({"body": post_html})
        return RenderedBlogFile(Path(post.path), content)
