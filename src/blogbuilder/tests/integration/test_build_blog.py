from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.blog_builder import BlogBuilder


class IntegrationBuildBlogTests(TestCase):
    def example_test_app_path(self) -> Path:
        return Path("src/blogbuilder/tests/example-test-app")

    def test_renders_given_blog_name(self) -> None:
        """
        given a blog name in the example dir
        it renders the blog name
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path(),
                output_dir,
            )

            with open(output_dir / "index.html") as post:
                assert "<title>Dat fancy blog</title>" in post.read()

    def test_build_example_index_page(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders the index page
        containing the post content
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path(),
                output_dir,
            )

            with open(output_dir / "index.html") as post:
                assert (
                    '<h1><a href="/post/cool-post.html">Nice post</a></h1>'
                    in post.read()
                )

    def test_build_example_blog_post(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with the post title
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path(),
                output_dir,
            )

            with open(output_dir / "post" / "cool-post.html") as post:
                assert (
                    '<h1><a href="/post/cool-post.html">Nice post</a></h1>'
                    in post.read()
                )

    def test_build_example_blog_with_template(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with base template
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path(),
                output_dir,
            )

            with open(output_dir / "post" / "cool-post.html") as post:
                assert "Some arbitrary template string" in post.read()

    def test_build_archive_page(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders the archive page
        and the month of the post
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path(),
                output_dir,
            )

            with open(output_dir / "archive.html") as post:
                assert "September 2021" in post.read()

    def test_build_about_page(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders the about page
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path(),
                output_dir,
            )

            with open(output_dir / "about.html") as post:
                assert "About cool blog" in post.read()
