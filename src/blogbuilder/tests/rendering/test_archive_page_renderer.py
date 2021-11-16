from pathlib import Path
from unittest import TestCase, mock

from blogbuilder.post_repository import PostArchive
from blogbuilder.rendering.archive_page_renderer import ArchivePageRenderer


class ArchivePageRendererTest(TestCase):
    def test_renders_archive_html_file(self) -> None:
        """
        it returns a file with path archive.html
        """
        result = ArchivePageRenderer(mock.Mock(), "nvm").render(mock.MagicMock())

        assert result.path == Path("archive.html")

    def test_renders_post_archive_months(self) -> None:
        """
        given a post archive
        it renders each month name
        """
        month = mock.Mock()
        month.name = "November 2021"
        archive: PostArchive = ((month, []),)

        result = ArchivePageRenderer(mock.Mock(), mock.Mock()).render(archive)

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

        result = ArchivePageRenderer(mock.Mock(), mock.Mock()).render(archive)

        assert post.url_path in result.content
        assert post.title in result.content
