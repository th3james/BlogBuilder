from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Template:
    template_str: str

    def render(self, values: Dict[str, str]) -> str:
        return "hello world"
