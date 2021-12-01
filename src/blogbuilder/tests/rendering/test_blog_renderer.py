from unittest import TestCase, mock

from blogbuilder.blog_data_reader import BlogDataReader
from blogbuilder.post_repository import PostRepository
from blogbuilder.rendering.about_page_renderer import AboutPageRenderer
from blogbuilder.rendering.archive_page_renderer import ArchivePageRenderer
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
        base_template = Template("<main> cool $body </main>")
        blog_data_reader = BlogDataReader(
            blog_name="cool blog name",
            post_repository=mock.MagicMock(),
            template_repository=TemplateRepository(base_template),
            about_text="",
        )

        blog_renderer = BlogRenderer(blog_data_reader)
        result = blog_renderer.render_all()

        assert (
            IndexPageRenderer(base_template, blog_data_reader.blog_name).render(
                blog_data_reader.post_repository
            )
            in result
        )

    def test_renderer_returns_file_for_post(self) -> None:
        """
        given a PostRepository with a post
        and a TemplateRepository with a base template
        it returns the rendered post
        """
        post = build_post()
        base_template = Template("<main> cool $body </main>")
        blog_data_reader = BlogDataReader(
            blog_name="hat",
            post_repository=PostRepository([post]),
            template_repository=TemplateRepository(base_template),
            about_text="",
        )

        blog_renderer = BlogRenderer(blog_data_reader)
        result = blog_renderer.render_all()

        assert (
            PostPageRenderer(base_template, blog_data_reader.blog_name).render(post)
            in result
        )

    def test_renderer_all_returns_archive(self) -> None:
        """
        it returns an enumerable containing rendered archive.html
        """
        base_template = Template("<main> cool $body </main>")
        post_repository = mock.MagicMock()
        blog_data_reader = BlogDataReader(
            blog_name=mock.Mock(),
            post_repository=post_repository,
            template_repository=TemplateRepository(base_template),
            about_text="",
        )

        blog_renderer = BlogRenderer(blog_data_reader)
        result = blog_renderer.render_all()

        assert (
            ArchivePageRenderer(base_template, blog_data_reader.blog_name).render(
                post_repository.archive.return_value
            )
            in result
        )

    def test_renderer_all_returns_about(self) -> None:
        """
        it returns an enumerable containing rendered about.html
        """
        base_template = Template("<main> cool $body </main>")
        post_repository = mock.MagicMock()
        blog_data_reader = BlogDataReader(
            blog_name=mock.Mock(),
            post_repository=post_repository,
            template_repository=TemplateRepository(base_template),
            about_text="",
        )

        blog_renderer = BlogRenderer(blog_data_reader)
        result = blog_renderer.render_all()

        assert (
            AboutPageRenderer(base_template, blog_data_reader.blog_name).render(
                blog_data_reader.about_text
            )
            in result
        )
