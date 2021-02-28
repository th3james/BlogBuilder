from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.blog_builder import BlogBuilder


class TestBlogBuilder(TestCase):
    def test_creates_output_directory(self) -> None:
        """
        given an output directory which doesn't exist
        it creates it
        """
        data_dir = Path("../test_output")
        templates_dir = Path("../test_output")
        output_dir = Path("../test_output")

        try:
            BlogBuilder().build(
                data_dir,
                templates_dir,
                output_dir,
            )

            assert output_dir.is_dir()
        finally:
            rmtree(output_dir)
