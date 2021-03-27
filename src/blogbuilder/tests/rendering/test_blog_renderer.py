from pathlib import Path
from unittest import mock, TestCase

from blogbuilder.post import Post
from blogbuilder.post_repository import PostRepository
from blogbuilder.rendering.blog_renderer import BlogRenderer
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.templates.template import Template
from blogbuilder.templates.template_repository import TemplateRepository


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
        and a TemplateRepository with a base template
        it returns the rendered post
        """
        post = Post("fancy-post", "")
        post_repository = PostRepository([post])
        base_template = Template("<main> cool $body </main>")
        template_repository = TemplateRepository(base_template)

        blog_renderer = BlogRenderer(post_repository, template_repository)
        result = blog_renderer.render_all()

        assert PostRenderer(base_template).render(post) in result