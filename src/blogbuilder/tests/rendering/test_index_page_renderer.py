from pathlib import Path
from unittest import mock, TestCase

from blogbuilder.rendering.index_page_renderer import IndexPageRenderer
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.templates.template import Template
from blogbuilder.tests.factories import build_post


class IndexPageRendererTest(TestCase):
    def test_renders_index_html_file(self) -> None:
        """
        it returns a file with path index.html
        """
        result = IndexPageRenderer(mock.Mock(), "nvm").render(mock.MagicMock())

        assert result.path == Path("index.html")

    def test_renders_recent_posts(self) -> None:
        """
        given a recent post provider
        it renders each post
        """
        base_template = Template("<main> I am template $body </main>")

        posts = [build_post(title="a"), build_post(title="b")]
        recent_post_provider = mock.Mock()
        recent_post_provider.recent_posts.return_value = posts

        result = IndexPageRenderer(base_template, "nvm").render(recent_post_provider)

        assert all([PostRenderer().render(post) in result.content for post in posts])

    def test_renders_using_base_template(self) -> None:
        """
        given a base template
        it renders the posts inside it
        """
        base_template = Template("<main> I am template $body </main>")

        result = IndexPageRenderer(base_template, "nvm").render(mock.MagicMock())

        assert "I am template" in result.content

    def test_renders_blog_name(self) -> None:
        """
        given a blog name
        it includes the blog name in the template
        """
        blog_name = "cool blog, innit?"
        base_template = Template("<title> I am template $blog_name</title>")

        result = IndexPageRenderer(base_template, blog_name).render(mock.MagicMock())

        assert blog_name in result.content
