from pathlib import Path
from unittest import TestCase, mock
from unittest.mock import call

from blogbuilder.blog_builder import BlogBuilder
from blogbuilder.blog_renderer import BlogRenderer
from blogbuilder.output_writer import OutputWriter


class TestBlogBuilder(TestCase):
    def test_loads_the_posts_then_renders_each_file(self) -> None:
        """
        given a valid data, template and output directory
        it loads the posts
        loads the templates
        renders the pages
        and writes them to the output directory
        """
        data_dir = Path("./nope")
        template_dir = Path("./nvm")
        output_dir = Path("./outno")

        fake_file_1 = mock.Mock()
        fake_file_2 = mock.Mock()

        FakePostRepository = mock.Mock()
        FakeTemplateRepository = mock.Mock()
        FakeBlogRenderer = mock.Mock(spec=BlogRenderer)
        FakeBlogRenderer.return_value.render_all.return_value = (
            fake_file_1,
            fake_file_2,
        )
        FakeOutputWriter = mock.Mock(spec=OutputWriter)

        with mock.patch.multiple(
            "blogbuilder.blog_builder",
            PostRepository=FakePostRepository,
            TemplateRepository=FakeTemplateRepository,
            BlogRenderer=FakeBlogRenderer,
            OutputWriter=FakeOutputWriter,
        ):
            BlogBuilder().build(data_dir, template_dir, output_dir)

        FakeOutputWriter.return_value.write.assert_has_calls(
            [call(fake_file_1), call(fake_file_2)]
        )
