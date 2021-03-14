from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.blog_file import BlogFile
from blogbuilder.output_writer import OutputWriter


class OutputWriterTests(TestCase):
    def test_write_creates_file(self) -> None:
        """
        given a file
        it creates it in the output directory
        """
        output_dir = Path("blogbuilder/tests/output_writer_test_data")
        blog_file = BlogFile(Path("nice-file.html"))

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
        blog_file = BlogFile(Path("nice-file.html"))

        try:
            output_dir = Path("blogbuilder/tests/output_writer_test_data")
            output_dir.mkdir(parents=True)

            output_writer = OutputWriter(output_dir)

            output_writer.write(blog_file)

            expected_file = output_dir / blog_file.path
            assert expected_file.is_file()
        finally:
            rmtree(output_dir)
