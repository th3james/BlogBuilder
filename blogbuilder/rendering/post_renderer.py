from pathlib import Path

from blogbuilder.post import Post
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer


class PostRenderer:
    def render(self, post: Post) -> RenderedBlogFile:
        content = MarkdownRenderer().render(post.body)
        return RenderedBlogFile(Path(post.slug + ".html"), content)
