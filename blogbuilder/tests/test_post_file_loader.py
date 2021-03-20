from pathlib import Path
from shutil import rmtree
from unittest import TestCase

from blogbuilder.post_file_loader import PostFileLoader


class PostFileLoaderTest(TestCase):
    def test_load_from_valid_file_chroots_path(self) -> None:
        """
        given a file
        it return a post with slug set based on file name
        """
        input_dir = Path("blogbuilder/tests/post_file_loader_tests_data")

        try:
            input_dir.mkdir(parents=True)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.touch()

            result = PostFileLoader(input_dir).load(post_file_path)

            assert result.slug == "fancy-post"
        finally:
            rmtree(input_dir)

    def test_load_from_valid_file_laods_body(self) -> None:
        """
        given a file
        it return a post with the body read from the file
        """
        input_dir = Path("blogbuilder/tests/post_file_loader_tests_data")
        body_text = "body text, yeah?"

        try:
            input_dir.mkdir(parents=True)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.write_text(body_text)

            result = PostFileLoader(input_dir).load(post_file_path)

            assert result.body == body_text
        finally:
            rmtree(input_dir)
