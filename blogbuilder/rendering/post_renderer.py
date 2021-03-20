from pathlib import Path

from blogbuilder.post import Post
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile


class PostRenderer:
    def render(self, post: Post) -> RenderedBlogFile:
        return RenderedBlogFile(Path(post.slug + ".html"), post.body)
