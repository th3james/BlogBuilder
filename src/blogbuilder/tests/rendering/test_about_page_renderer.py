from pathlib import Path
from unittest import TestCase

from blogbuilder.rendering.about_page_renderer import AboutPageRenderer
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer
from blogbuilder.templates.template import Template


class AboutPageRendererTest(TestCase):
    def test_renders_about_html_file(self) -> None:
        """
        it returns a file with path about.html
        """
        result = AboutPageRenderer(Template("$body"), "nvm").render("whatever")

        assert result.path == Path("about.html")

    def test_renders_about_text_as_html(self) -> None:
        """
        it returns a file with path about.html
        """
        about_text = "# Markdown\n* is fun"
        result = AboutPageRenderer(Template("$body"), "nvm").render(about_text)

        assert result.content in MarkdownRenderer().render(about_text)

    def test_renders_page_title(self) -> None:
        """
        given a blog name
        it renders the page title as blog_name | About
        """
        base_template = Template("<title>$page_title</title>")

        result = AboutPageRenderer(base_template, "Cool blog").render("not important")

        assert "Cool blog | About" in result.content
