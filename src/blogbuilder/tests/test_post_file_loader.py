from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock, TestCase

import pytest

from blogbuilder.post_file_loader import PostFileLoader, InvalidPostDefinitionError
from blogbuilder.tests.factories import build_valid_post_content


class PostFileLoaderTest(TestCase):
    def test_load_from_valid_file_chroots_path(self) -> None:
        """
        given a file
        it return a post with slug set based on file name
        """
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.write_text(build_valid_post_content())

            result = PostFileLoader(input_dir).load(post_file_path)

            assert result.slug == "fancy-post"

    def test_load_from_valid_file_loads_attributes_from_content(self) -> None:
        """
        given a file
        it parses the post fields from the file content
        """
        file_content = """title: nvm
body:
text, yeah?"""
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            post_file_path = input_dir / "fancy-post.md"
            post_file_path.write_text(file_content)

            post_file_loader = PostFileLoader(input_dir)
            result = post_file_loader.load(post_file_path)

            core_fields = post_file_loader.parse_str(file_content)
            assert result.body == core_fields.body
            assert result.title == core_fields.title

    def test_parse_str_parses_body(self) -> None:
        """
        given a string with a valid body: attribute
        it return a post with the body set correctly
        """
        body = "text, yeah?"
        file_content = build_valid_post_content(body=body)

        result = PostFileLoader(mock.Mock()).parse_str(file_content)

        assert result.body == body

    def test_parse_str_fails_when_no_body(self) -> None:
        """
        given a string without valid body: attribute
        it returns a meaningful error
        """
        with pytest.raises(InvalidPostDefinitionError):
            PostFileLoader(mock.Mock()).parse_str("title: nvm")

    def test_parse_str_parses_title(self) -> None:
        """
        given a string with a valid title: attribute
        it return a post with the title set correctly
        """
        title = "title, yeah?"
        file_content = build_valid_post_content(title=title)

        result = PostFileLoader(mock.Mock()).parse_str(file_content)

        assert result.title == title

    def test_parse_str_fails_when_no_title(self) -> None:
        """
        given a string without valid title: attribute
        it returns a meaningful error
        """
        with pytest.raises(InvalidPostDefinitionError):
            PostFileLoader(mock.Mock()).parse_str("body:\nnvm")
