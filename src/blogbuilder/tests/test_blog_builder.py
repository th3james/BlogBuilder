from pathlib import Path
from unittest import TestCase, mock
from unittest.mock import call

from blogbuilder.blog_builder import BlogBuilder
from blogbuilder.blog_data_reader import BlogDataReader
from blogbuilder.output_writer import OutputWriter
from blogbuilder.rendering.blog_renderer import BlogRenderer


class BlogBuilderTests(TestCase):
    def test_loads_the_posts_then_renders_each_file(self) -> None:
        """
        given a input and output directory
        it loads blog data
        renders the pages
        and writes them to the output directory
        """
        input_dir = Path("./input_no")
        output_dir = Path("./out_no")

        fake_file_1 = mock.Mock()
        fake_file_2 = mock.Mock()

        FakeBlogDataReaderCls = mock.Mock()
        fake_blog_data_reader = mock.Mock(spec=BlogDataReader)
        FakeBlogDataReaderCls.load_from_directory.return_value = fake_blog_data_reader

        FakeBlogRenderer = mock.Mock(spec=BlogRenderer)
        FakeBlogRenderer.return_value.render_all.return_value = (
            fake_file_1,
            fake_file_2,
        )
        FakeOutputWriter = mock.Mock(spec=OutputWriter)

        with mock.patch.multiple(
            "blogbuilder.blog_builder",
            BlogDataReader=FakeBlogDataReaderCls,
            BlogRenderer=FakeBlogRenderer,
            OutputWriter=FakeOutputWriter,
        ):
            BlogBuilder().build(input_dir, output_dir)

        FakeBlogDataReaderCls.load_from_directory.assert_called_once_with(input_dir)

        FakeBlogRenderer.assert_called_once_with(fake_blog_data_reader)

        FakeOutputWriter.assert_called_once_with(output_dir)

        FakeOutputWriter.return_value.write.assert_has_calls(
            [call(fake_file_1), call(fake_file_2)]
        )
