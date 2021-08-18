from typing import TYPE_CHECKING

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer

if TYPE_CHECKING:
    from blogbuilder.post import Post


class PostRenderer:
    def render(self, post: "Post") -> str:
        post_markdown = f"# [{post.title}]({post.path})\n{post.body}"
        return MarkdownRenderer().render(post_markdown)
