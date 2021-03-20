from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.output_writer import OutputWriter


class OutputWriterTests(TestCase):
    def test_write_creates_file(self) -> None:
        """
        given a file
        it creates it in the output directory
        """
        output_dir = Path("blogbuilder/tests/output_writer_test_data")
        blog_file = RenderedBlogFile(Path("nice-file.html"), "")

        try:
            output_writer = OutputWriter(output_dir)

            output_writer.write(blog_file)

            expected_file = output_dir / blog_file.path
            assert expected_file.is_file()
        finally:
            rmtree(output_dir)

    def test_write_handles_pre_existing_dir(self) -> None:
        """
        given an output directory that already exists
        it creates it in the pre-existing directory
        """
        output_dir = Path("blogbuilder/tests/output_writer_test_data")
        blog_file = RenderedBlogFile(Path("nice-file.html"), "")

        try:
            output_dir = Path("blogbuilder/tests/output_writer_test_data")
            output_dir.mkdir(parents=True)

            output_writer = OutputWriter(output_dir)

            output_writer.write(blog_file)

            expected_file = output_dir / blog_file.path
            assert expected_file.is_file()
        finally:
            rmtree(output_dir)

    def test_write_writes_file_content(self) -> None:
        """
        given a file
        it writes the content to the file
        """
        output_dir = Path("blogbuilder/tests/output_writer_test_data")
        content = "some text or whatever"
        blog_file = RenderedBlogFile(Path("nice-file.html"), content)

        try:
            output_writer = OutputWriter(output_dir)

            output_writer.write(blog_file)

            expected_file = output_dir / blog_file.path
            assert expected_file.read_text() == content
        finally:
            rmtree(output_dir)
