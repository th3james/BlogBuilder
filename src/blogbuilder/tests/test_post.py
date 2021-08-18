from unittest import TestCase

from blogbuilder.tests.factories import build_post


class PostTest(TestCase):
    def test_path_includes_slug(self) -> None:
        """
        it prepends "post/" to the slug
        """
        post = build_post(slug="cool-slug")
        assert "/post/cool-slug" == post.path
