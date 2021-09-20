from unittest import mock, TestCase

from blogbuilder.post_repository import PostRepository
from blogbuilder.rendering.blog_renderer import BlogRenderer
from blogbuilder.rendering.index_page_renderer import IndexPageRenderer
from blogbuilder.rendering.post_page_renderer import PostPageRenderer
from blogbuilder.templates.template import Template
from blogbuilder.templates.template_repository import TemplateRepository
from blogbuilder.tests.factories import build_post


class BlogRendererTest(TestCase):
    def test_renderer_all_returns_index(self) -> None:
        """
        it returns an enumerable containing rendered index.html
        """
        blog_name = "cool blog name"
        post_repository = mock.MagicMock()
        base_template = Template("<main> cool $body </main>")
        template_repository = TemplateRepository(base_template)

        blog_renderer = BlogRenderer(blog_name, post_repository, template_repository)
        result = blog_renderer.render_all()

        assert (
            IndexPageRenderer(base_template, blog_name).render(post_repository)
            in result
        )

    def test_renderer_returns_file_for_post(self) -> None:
        """
        given a PostRepository with a post
        and a TemplateRepository with a base template
        it returns the rendered post
        """
        blog_name = "name of the blog, yeah"
        post = build_post()
        post_repository = PostRepository([post])
        base_template = Template("<main> cool $body </main>")
        template_repository = TemplateRepository(base_template)

        blog_renderer = BlogRenderer(mock.Mock(), post_repository, template_repository)
        result = blog_renderer.render_all()

        assert PostPageRenderer(base_template, blog_name).render(post) in result
