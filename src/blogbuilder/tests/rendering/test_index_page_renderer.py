from pathlib import Path
from unittest import mock, TestCase

from blogbuilder.post import Post
from blogbuilder.rendering.index_page_renderer import IndexPageRenderer
from blogbuilder.templates.template import Template


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
        base_template = Template("<main> I am template $body </main>")

        post_slugs = ["cool", "whatever"]
        recent_post_provider = mock.Mock()
        recent_post_provider.recent_posts.return_value = [
            Post(slug, "nvm") for slug in post_slugs
        ]

        result = IndexPageRenderer(base_template).render(recent_post_provider)

        assert all([slug in result.content for slug in post_slugs])

    def test_renders_using_base_template(self) -> None:
        """
        given a base template
        it renders the posts inside it
        """
        base_template = Template("<main> I am template $body </main>")

        result = IndexPageRenderer(base_template).render(mock.MagicMock())

        assert "I am template" in result.content
