from dataclasses import dataclass
from pathlib import Path

from blogbuilder.post import Post


class InvalidPostDefinitionError(Exception):
    pass


@dataclass(frozen=True)
class PostFileLoader:
    base_input_dir: Path

    def load(self, input_file_path: Path) -> Post:
        chrooted_path = input_file_path.relative_to(self.base_input_dir)

        file_content = input_file_path.read_text()
        core_post = self.parse_str(file_content)

        return Post(chrooted_path.stem, core_post.title, core_post.body)

    def parse_str(self, post_str: str) -> Post:
        split_content = post_str.split("title: ")
        if len(split_content) == 1:
            raise InvalidPostDefinitionError(
                "Couldn't parse required field 'title' in:\n" + post_str
            )

        title = split_content[1].split("\n")[0]

        split_content = post_str.split("body:\n")
        if len(split_content) == 1:
            raise InvalidPostDefinitionError(
                "Couldn't parse required field 'body' in:\n" + post_str
            )

        body = split_content[1]
        return Post("not implemented", title, body)
