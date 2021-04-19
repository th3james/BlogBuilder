from pathlib import Path
from unittest import mock, TestCase

from blogbuilder.post import Post
from blogbuilder.rendering.index_page_renderer import IndexPageRenderer
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer


class IndexPageRendererTest(TestCase):
    def test_renders_index_html_file(self) -> None:
        """
        it returns a file with path index.html
        """
        result = IndexPageRenderer(mock.Mock()).render(mock.MagicMock())

        assert result.path == Path("index.html")

    def test_renders_recent_post_slugs(self) -> None:
        """
        given a recent post provider
        it renders the slugs of the recent posts
        """
        post_slugs = ["cool", "whatever"]
        recent_post_provider = mock.Mock()
        recent_post_provider.recent_posts.return_value = [
            Post(slug, "nvm") for slug in post_slugs
        ]

        result = IndexPageRenderer(mock.Mock()).render(recent_post_provider)

        assert all([slug in result.content for slug in post_slugs])

    def test_renders_rendered_markdown_content_of_recent(self) -> None:
        """
        given a recent post provider
        it renders the  of the recent posts
        """
        post_bodies = ["cool", "whatever"]
        recent_post_provider = mock.Mock()
        recent_post_provider.recent_posts.return_value = [
            Post("shrug", body) for body in post_bodies
        ]

        result = IndexPageRenderer(mock.Mock()).render(recent_post_provider)

        assert all(
            [MarkdownRenderer().render(body) in result.content for body in post_bodies]
        )
