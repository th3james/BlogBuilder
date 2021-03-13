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
        output_dir = Path("blogbuilder/tests/test_output")
        blog_file = BlogFile(Path("nice-file.html"))

        try:
            output_writer = OutputWriter(output_dir)

            output_writer.write(blog_file)

            expected_file = output_dir / blog_file.path
            assert expected_file.is_file()
        finally:
            rmtree(output_dir)
