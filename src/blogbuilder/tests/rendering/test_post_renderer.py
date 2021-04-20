from unittest import TestCase

from blogbuilder.post import Post
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer
from blogbuilder.rendering.post_renderer import PostRenderer


class PostRendererTest(TestCase):
    def test_renders_post_content_as_rendered_markdown(self) -> None:
        """
        given a post
        it returns a string containing the post content rendered as markdown
        """
        post = Post("nvm", "nvm", "## Some markdown")

        result = PostRenderer().render(post)

        assert MarkdownRenderer().render(post.body) in result
