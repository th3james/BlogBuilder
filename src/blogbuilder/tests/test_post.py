from pathlib import Path
from unittest import TestCase

from blogbuilder.tests.factories import build_post


class PostTest(TestCase):
    def test_file_path_is_based_on_slug(self) -> None:
        """
        it returns a path based on the slug
        """
        post = build_post(slug="cool-slug")
        assert Path("./post/cool-slug.html") == post.file_path

    def test_url_path_is_based_on_slug(self) -> None:
        """
        it returns a string with "/post" prepended
        """
        post = build_post(slug="cool-slug")
        assert "/post/cool-slug.html" == post.url_path
