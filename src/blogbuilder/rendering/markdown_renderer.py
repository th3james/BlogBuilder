import mistletoe  # type: ignore
from typing import cast

from blogbuilder.rendering.pygments_renderer import PygmentsRenderer  # type: ignore


class MarkdownRenderer:
    def render(self, markdown_str: str) -> str:
        return cast(str, mistletoe.markdown(markdown_str, PygmentsRenderer))
