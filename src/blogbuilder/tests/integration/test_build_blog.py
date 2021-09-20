from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.blog_builder import BlogBuilder


class IntegrationBuildBlogTests(TestCase):
    def example_test_app_path(self) -> Path:
        return Path("src/blogbuilder/tests/example-test-app")

    def test_renders_given_blog_name(self) -> None:
        """
        given a blog name
        it renders the blog name
        """
        blog_name = "Dat fancy blog"
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                blog_name,
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
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
                "Cool blog name",
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
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
                "Cool blog name",
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
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
                "Cool blog name",
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
                output_dir,
            )

            with open(output_dir / "post" / "cool-post.html") as post:
                assert "Some arbitrary template string" in post.read()
