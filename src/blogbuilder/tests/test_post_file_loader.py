from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.post_file_loader import PostFileLoader


class PostFileLoaderTest(TestCase):
    def test_load_from_valid_file_chroots_path(self) -> None:
        """
        given a file
        it return a post with slug set based on file name
        """
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.touch()

            result = PostFileLoader(input_dir).load(post_file_path)

            assert result.slug == "fancy-post"

    def test_load_from_valid_file_loads_body(self) -> None:
        """
        given a file
        it return a post with the body read from the file
        """
        body_text = "body text, yeah?"
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.write_text(body_text)

            result = PostFileLoader(input_dir).load(post_file_path)

            assert result.body == body_text
