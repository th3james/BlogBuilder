from dataclasses import dataclass
from pathlib import Path

from blogbuilder.rendering.markdown_renderer import MarkdownRenderer
from blogbuilder.post_repository import PostArchive
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class ArchivePageRenderer:
    base_template: Template
    blog_name: str

    def render(self, post_archive: PostArchive) -> RenderedBlogFile:
        md_content = ""
        for month, posts in post_archive:
            md_content += f"## {month.name}\n\n"
            for post in posts:
                md_content += f"* [{post.title}]({post.url_path})"

        content = MarkdownRenderer().render(md_content)

        return RenderedBlogFile(Path("archive.html"), content)
