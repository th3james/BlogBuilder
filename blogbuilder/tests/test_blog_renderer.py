from pathlib import Path
from unittest import mock, TestCase

from blogbuilder.blog_renderer import BlogRenderer
from blogbuilder.post import Post
from blogbuilder.post_repository import PostRepository


class BlogRendererTest(TestCase):
    def test_renderer_all_returns_index(self) -> None:
        """
        it returns an enumerable containing index.html
        """
        blog_renderer = BlogRenderer(mock.MagicMock(), mock.Mock())

        result = blog_renderer.render_all()

        assert Path("index.html") in [p.path for p in result]

    def test_renderer_returns_file_for_post(self) -> None:
        """
        given a PostRepository with a post
        it returns a file with the post path
        """
        post = Post(Path("fancy-post.html"), Path("fancy-post.html"))
        post_repository = mock.Mock(spec=PostRepository)
        post_repository.get_all.return_value = [post]

        blog_renderer = BlogRenderer(post_repository, mock.Mock())
        result = blog_renderer.render_all()

        assert post.path in [p.path for p in result]
