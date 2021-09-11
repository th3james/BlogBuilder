from datetime import datetime
from unittest import TestCase

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.tests.factories import build_post


class PostRendererTest(TestCase):
    def test_renders_post_content_as_rendered_markdown(self) -> None:
        """
        given a post
        it returns a string containing the post content rendered as markdown
        """
        post = build_post(body="## Some markdown")

        result = PostRenderer().render(post)

        assert MarkdownRenderer().render(post.body) in result

    def test_renders_post_title(self) -> None:
        """
        given a post
        it returns a string containing the post title in h1 tags
        """
        post = build_post(title="wicked nice title")

        result = PostRenderer().render(post)

        expected_title = f'<h1><a href="{post.url_path}">wicked nice title</a></h1>'
        assert expected_title in result

    def test_renders_friendly_post_timestamp(self) -> None:
        """
        given a post
        it returns html with a human friendly date
        """
        post = build_post(timestamp=datetime.fromisoformat("2021-02-24T09:47+00:00"))

        result = PostRenderer().render(post)

        assert "February 24, 2021" in result

    def test_renders_machine_post_timestamp(self) -> None:
        """
        given a post
        it returns html with the isodate for machine parsing
        """
        timestamp_iso_str = "2020-10-04T00:49:00+00:00"
        post = build_post(timestamp=datetime.fromisoformat(timestamp_iso_str))

        result = PostRenderer().render(post)

        assert timestamp_iso_str in result
