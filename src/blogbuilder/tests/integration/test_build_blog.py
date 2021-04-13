from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.blog_builder import BlogBuilder


class IntegrationBuildBlogTests(TestCase):
    def example_test_app_path(self) -> Path:
        return Path("src/blogbuilder/tests/example-test-app")

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
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
                output_dir,
            )

            with open(output_dir / "index.html") as post:
                assert "<h1>Nice post</h1>" in post.read()

    def test_build_example_blog_post(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with the post title
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
                output_dir,
            )

            with open(output_dir / "cool-post.html") as post:
                assert "<h1>Nice post</h1>" in post.read()

    def test_build_example_blog_with_template(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with base template
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                self.example_test_app_path() / Path("posts"),
                self.example_test_app_path() / Path("templates"),
                output_dir,
            )

            with open(output_dir / "cool-post.html") as post:
                assert "<header>Dat blog title</header>" in post.read()
