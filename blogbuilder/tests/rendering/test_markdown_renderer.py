from unittest import TestCase

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer


class MarkdownRendererTest(TestCase):
    def test_render_renders_headers(self) -> None:
        """
        given a source string with a header
        it converts it to a header tag
        """
        assert "<h1>Nice header</h1>" == MarkdownRenderer().render("# Nice header")
