from dataclasses import dataclass
from typing import Iterable, List

from blogbuilder.blog_data_reader import BlogDataReader
from blogbuilder.rendering.archive_page_renderer import ArchivePageRenderer
from blogbuilder.rendering.index_page_renderer import IndexPageRenderer
from blogbuilder.rendering.post_page_renderer import PostPageRenderer
from blogbuilder.rendering.rendered_blog_file import RenderedBlogFile


@dataclass(frozen=True)
class BlogRenderer:
    blog_data_reader: BlogDataReader

    def render_all(self) -> Iterable[RenderedBlogFile]:
        index_page = IndexPageRenderer(
            self.blog_data_reader.template_repository.base_template,
            self.blog_data_reader.blog_name,
        ).render(self.blog_data_reader.post_repository)

        archive_page = ArchivePageRenderer(
            self.blog_data_reader.template_repository.base_template,
            self.blog_data_reader.blog_name,
        ).render(self.blog_data_reader.post_repository.archive())

        files: List[RenderedBlogFile] = [index_page, archive_page]
        for post in self.blog_data_reader.post_repository.posts:
            files.append(
                PostPageRenderer(
                    self.blog_data_reader.template_repository.base_template,
                    self.blog_data_reader.blog_name,
                ).render(post)
            )
        return files
