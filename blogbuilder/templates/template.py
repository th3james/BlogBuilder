from dataclasses import dataclass
from string import Template as StdLibTemplate
from typing import Dict


class MissingTemplateValueError(Exception):
    pass


@dataclass(frozen=True)
class Template:
    template_str: str

    def render(self, values: Dict[str, str]) -> str:
        try:
            return StdLibTemplate(self.template_str).substitute(**values)
        except KeyError as err:
            raise MissingTemplateValueError(f"Missing template value {err}")
