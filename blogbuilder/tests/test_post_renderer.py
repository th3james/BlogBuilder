from pathlib import Path
from unittest import TestCase

from blogbuilder.post import Post
from blogbuilder.post_renderer import PostRenderer


class PostRendererTest(TestCase):
    def test_render_path_based_on_slug(self) -> None:
        """
        given a post
        it returns a rendered file with the path based on the slug
        """
        post = Post("dope-file", "")

        result = PostRenderer().render(post)

        assert Path("dope-file.html") == result.path

    def test_render_renders_content(self) -> None:
        """
        given a post
        it returns a rendered file with the content based on the body
        """
        post = Post("dope-file", "nice text")

        result = PostRenderer().render(post)

        assert "nice text" == result.content
