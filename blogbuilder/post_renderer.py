from pathlib import Path

from blogbuilder.post import Post
from blogbuilder.rendered_blog_file import RenderedBlogFile


class PostRenderer:
    def render(self, post: Post) -> RenderedBlogFile:
        return RenderedBlogFile(Path(post.slug + ".html"))
