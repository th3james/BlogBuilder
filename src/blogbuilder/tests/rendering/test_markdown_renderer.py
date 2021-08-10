from unittest import TestCase

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer


class MarkdownRendererTest(TestCase):
    def test_render_renders_headers(self) -> None:
        """
        given a source string with a header
        it converts it to a header tag
        """
        assert "<h1>Nice header</h1>\n" == MarkdownRenderer().render("# Nice header")

    def test_render_renders_lang_code_blocks(self) -> None:
        """
        given a source string with an language annotated code block
        it renders a valid code block
        """
        input_markdown = """```python
    print('sup')
"""
        expected_html = """<pre><code class="language-python">    print('sup')
</code></pre>
"""
        assert expected_html == MarkdownRenderer().render(input_markdown)
