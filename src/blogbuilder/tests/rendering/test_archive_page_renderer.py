from pathlib import Path
from unittest import TestCase, mock

from blogbuilder.post_repository import PostArchive
from blogbuilder.rendering.archive_page_renderer import ArchivePageRenderer
from blogbuilder.templates.template import Template


class ArchivePageRendererTest(TestCase):
    def test_renders_archive_html_file(self) -> None:
        """
        it returns a file with path archive.html
        """
        result = ArchivePageRenderer(Template("$body"), "nvm").render(mock.MagicMock())

        assert result.path == Path("archive.html")

    def test_renders_post_archive_months(self) -> None:
        """
        given a post archive
        it renders each month name
        """
        month = mock.Mock()
        month.name = "November 2021"
        archive: PostArchive = ((month, []),)

        result = ArchivePageRenderer(Template("$body"), mock.Mock()).render(archive)

        assert month.name in result.content

    def test_renders_post_archive_posts(self) -> None:
        """
        given a post archive
        it renders a link to each post
        """

        month = mock.Mock()
        month.name = "Octoberry"
        post = mock.Mock()
        post.title = "Swag post"
        post.url_path = "/posts/whatever.html"
        archive: PostArchive = ((month, [post]),)

        result = ArchivePageRenderer(Template("$body"), mock.Mock()).render(archive)

        assert post.url_path in result.content
        assert post.title in result.content

    def test_renders_using_base_template(self) -> None:
        """
        given a base template
        it renders the archive in it
        """
        base_template = Template("<main> I am template $body </main>")

        result = ArchivePageRenderer(base_template, "nvm").render([])

        assert "I am template" in result.content
