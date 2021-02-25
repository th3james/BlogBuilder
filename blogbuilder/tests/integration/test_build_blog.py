from pathlib import Path

from blogbuilder.blogbuilder import BlogBuilder


class TestIntegrationBuildBlog:
    def test_build_example_blog(self) -> None:
        """
        given the example blog directory
        and an output directory
        it renders a page with the title
        """
        BlogBuilder.build(
            Path("../example-test-app/posts", "../example-test-app/templates")
        )
