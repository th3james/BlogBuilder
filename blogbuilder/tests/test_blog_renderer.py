from pathlib import Path
from unittest import mock, TestCase

from blogbuilder.blog_renderer import BlogRenderer


class BlogRendererTest(TestCase):
    def test_return_all_returns_index(self) -> None:
        """
        it returns an enumerable containing index.html
        """
        blog_renderer = BlogRenderer(mock.Mock(), mock.Mock())

        result = blog_renderer.render_all()

        assert Path("index.html") in [p.path for p in result]
