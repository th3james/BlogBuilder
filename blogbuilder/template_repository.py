from dataclasses import dataclass
from pathlib import Path

from blogbuilder.templates.template import Template


@dataclass(frozen=True)
class TemplateRepository:
    base_template: Template

    @classmethod
    def load_from_directory(cls, templates_dir: Path) -> "TemplateRepository":
        pass
