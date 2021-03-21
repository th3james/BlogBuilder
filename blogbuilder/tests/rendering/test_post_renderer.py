from pathlib import Path
from unittest import TestCase

from blogbuilder.post import Post
from blogbuilder.templates.template import Template
from blogbuilder.rendering.post_renderer import PostRenderer
from blogbuilder.rendering.markdown_renderer import MarkdownRenderer


class PostRendererTest(TestCase):
    def test_render_path_based_on_slug(self) -> None:
        """
        given a post
        it returns a rendered file with the path based on the slug
        """
        post = Post("dope-file", "")

        result = PostRenderer(Template("")).render(post)

        assert Path("dope-file.html") == result.path

    def test_render_renders_markdown_in_template(self) -> None:
        """
        given a post
        it returns a file with the content as rendered post body
        interpolated into the base template
        """
        base_template = Template("<main>sup $body</main>")
        post = Post("dope-file", "# nice text")

        result = PostRenderer(base_template).render(post)

        assert (
            base_template.render({"body": MarkdownRenderer().render(post.body)})
            == result.content
        )
