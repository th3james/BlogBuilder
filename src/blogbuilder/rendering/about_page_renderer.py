from dataclasses import dataclass
from pathlib import Path

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class AboutPageRenderer:
    base_template: Template
    blog_name: str

    def render(self, about_text: str) -> RenderedBlogFile:
        body_content = MarkdownRenderer().render(about_text)
        content = self.base_template.render(
            {
                "page_title": f"{self.blog_name} | About",
                "blog_name": self.blog_name,
                "body": body_content,
            }
        )
        return RenderedBlogFile(Path("about.html"), content)
