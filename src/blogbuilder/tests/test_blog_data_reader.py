from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, mock

from blogbuilder.blog_data_reader import BlogDataReader


class BlogDataReaderTests(TestCase):
    def test_load_from_directory_loads_blog_name(self) -> None:
        """
        given a directory containing a blog_name.txt
        it sets blog name correctly
        """
        blog_name = "Bob Loblaw's Law Blog"
        with TemporaryDirectory() as td:
            base_dir = Path(td)

            blog_name_file = base_dir / "blog_name.txt"
            blog_name_file.write_text(blog_name)

            with mock.patch.multiple(
                "blogbuilder.blog_data_reader",
                PostRepository=mock.Mock(),
                TemplateRepository=mock.Mock(),
            ):
                result = BlogDataReader.load_from_directory(base_dir)

                assert result.blog_name == blog_name

    def test_load_from_directory_strips_blog_name_whitespace(self) -> None:
        """
        given a blog name with a trailing line brea
        it strips it from the returned blog name
        """
        blog_name = "Bob Loblaw's Law Blog"
        with TemporaryDirectory() as td:
            base_dir = Path(td)

            blog_name_file = base_dir / "blog_name.txt"
            blog_name_file.write_text(blog_name + "\n")

            with mock.patch.multiple(
                "blogbuilder.blog_data_reader",
                PostRepository=mock.Mock(),
                TemplateRepository=mock.Mock(),
            ):
                result = BlogDataReader.load_from_directory(base_dir)

                assert result.blog_name == blog_name

    def test_load_from_directory_loads_post_repo(self) -> None:
        """
        given a directory containing a posts dir
        it builds a post repository
        """
        FakePostRepository = mock.Mock()

        with TemporaryDirectory() as td:
            base_dir = Path(td)

            blog_name_file = base_dir / "blog_name.txt"
            blog_name_file.write_text("nvm")

            with mock.patch.multiple(
                "blogbuilder.blog_data_reader",
                PostRepository=FakePostRepository,
                TemplateRepository=mock.Mock(),
            ):
                result = BlogDataReader.load_from_directory(base_dir)

                assert (
                    result.post_repository
                    == FakePostRepository.load_from_directory.return_value
                )
                FakePostRepository.load_from_directory.assert_called_once_with(
                    base_dir / "posts"
                )

    def test_load_from_directory_loads_templates_repository(self) -> None:
        """
        given a directory containing a templates dir
        it builds a template repository
        """
        FakeTemplateRepository = mock.Mock()

        with TemporaryDirectory() as td:
            base_dir = Path(td)

            blog_name_file = base_dir / "blog_name.txt"
            blog_name_file.write_text("nvm")

            with mock.patch.multiple(
                "blogbuilder.blog_data_reader",
                PostRepository=mock.Mock(),
                TemplateRepository=FakeTemplateRepository,
            ):
                result = BlogDataReader.load_from_directory(base_dir)

                assert (
                    result.template_repository
                    == FakeTemplateRepository.load_from_directory.return_value
                )
                FakeTemplateRepository.load_from_directory.assert_called_once_with(
                    base_dir / "templates"
                )
