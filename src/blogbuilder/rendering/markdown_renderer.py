from commonmark import commonmark


class MarkdownRenderer:
    def render(self, markdown_str: str) -> str:
        return commonmark(markdown_str)
