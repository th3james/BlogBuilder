from typing import TYPE_CHECKING

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer

if TYPE_CHECKING:
    from blogbuilder.post import Post


class PostRenderer:
    def render(self, post: "Post") -> str:
        post_time = post.timestamp.isoformat()
        post_markdown = f"""# [{post.title}]({post.url_path})
<time datetime="{post_time}">{post_time}</time>
{post.body}"""
        return MarkdownRenderer().render(post_markdown)
