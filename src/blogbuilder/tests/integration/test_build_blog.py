from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.blog_builder import BlogBuilder


class IntegrationBuildBlogTests(TestCase):
    def test_build_example_blog_post(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with the post title
        """
        with TemporaryDirectory() as td:
            output_dir = Path(td)
            BlogBuilder().build(
                Path("src/blogbuilder/tests/example-test-app/posts"),
                Path("src/blogbuilder/tests/example-test-app/templates"),
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
                Path("src/blogbuilder/tests/example-test-app/posts"),
                Path("src/blogbuilder/tests/example-test-app/templates"),
                output_dir,
            )

            with open(output_dir / "cool-post.html") as post:
                assert "<header>Dat blog title</header>" in post.read()
