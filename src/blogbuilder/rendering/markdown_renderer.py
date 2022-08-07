import mistletoe

from blogbuilder.rendering.pygments_renderer import PygmentsRenderer


class MarkdownRenderer:
    def render(self, markdown_str: str) -> str:
        return mistletoe.markdown(markdown_str, PygmentsRenderer)
