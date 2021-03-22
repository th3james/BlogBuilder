from dataclasses import dataclass
from pathlib import Path

from blogbuilder.templates.template import Template


class MissingTemplateError(Exception):
    pass


@dataclass(frozen=True)
class TemplateRepository:
    base_template: Template

    @classmethod
    def load_from_directory(cls, templates_dir: Path) -> "TemplateRepository":
        base_template_path = templates_dir / "base.tmpl"
        try:
            return cls(Template(base_template_path.read_text()))
        except FileNotFoundError:
            raise MissingTemplateError(
                f"Couldn't find template 'base.tmpl' in {templates_dir}"
            )
