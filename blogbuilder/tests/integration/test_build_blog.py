from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.blog_builder import BlogBuilder


class IntegrationBuildBlogTests(TestCase):
    def test_build_example_blog(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with the title
        """
        output_dir = Path("blogbuilder/tests/test_output")
        try:
            BlogBuilder().build(
                Path("../example-test-app/posts"),
                Path("../example-test-app/templates"),
                output_dir,
            )

            with open(output_dir / "cool-post.html") as post:
                assert "Nice post" in post.read()
        finally:
            rmtree(output_dir)
