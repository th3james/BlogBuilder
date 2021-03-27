from markdown import markdown


class MarkdownRenderer:
    def render(self, markdown_str: str) -> str:
        return markdown(markdown_str)
