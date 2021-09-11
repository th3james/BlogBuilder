from typing import TYPE_CHECKING

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer

if TYPE_CHECKING:
    from blogbuilder.post import Post


class PostRenderer:
    def render(self, post: "Post") -> str:
        post_machine_time = post.timestamp.isoformat()
        post_human_time = post.timestamp.strftime("%B %d, %Y")
        post_markdown = f"""# [{post.title}]({post.url_path})
<time datetime="{post_machine_time}">{post_human_time}</time>
{post.body}"""
        return MarkdownRenderer().render(post_markdown)
