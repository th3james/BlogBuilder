from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post_repository import PostArchive
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile
from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class ArchivePageRenderer:
    base_template: Template
    blog_name: str

    def render(self, post_archive: PostArchive) -> RenderedBlogFile:
        content = ""
        for month, _ in post_archive:
            content += month.name

        return RenderedBlogFile(Path("archive.html"), content)
