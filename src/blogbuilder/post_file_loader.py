from dataclasses import dataclass
from datetime import datetime
import re
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

        return Post(
            chrooted_path.stem, core_post.title, core_post.body, core_post.timestamp
        )

    def _parse_attribute(self, attribute: str, post_str: str) -> str:
        matches = re.findall(rf"^{attribute}: (.*)\n", post_str, flags=re.MULTILINE)
        if len(matches) == 0:
            raise InvalidPostDefinitionError(
                f"Couldn't parse required field '{attribute}' in:\n" + post_str
            )
        return str(matches[0])

    def parse_str(self, post_str: str) -> Post:
        title = self._parse_attribute("title", post_str)

        timestamp_str = self._parse_attribute("timestamp", post_str)
        timestamp = datetime.fromisoformat(timestamp_str)

        split_content = re.split(r"^body:\n", post_str, flags=re.MULTILINE)
        if len(split_content) == 1:
            raise InvalidPostDefinitionError(
                "Couldn't parse required field 'body' in:\n" + post_str
            )

        body = split_content[1]
        return Post("not implemented", title, body, timestamp)
