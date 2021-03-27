from pathlib import Path
import pytest
from tempfile import TemporaryDirectory
from unittest import TestCase

from blogbuilder.templates.template import Template
from blogbuilder.templates.template_repository import (
    TemplateRepository,
    MissingTemplateError,
)


class TemplateRepositoryTest(TestCase):
    def test_load_from_directory_when_directory_has_no_base_template(self) -> None:
        """
        given a directory not containing base.tmpl
        it raises MissingTemplateError
        """
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            with pytest.raises(MissingTemplateError, match=r".*base.tmpl.*"):
                TemplateRepository.load_from_directory(input_dir)

    def test_load_from_directory_with_base_template_loads_it(self) -> None:
        """
        given a directory not containing base.tmpl
        it raises MissingTemplateError
        """
        template_str = "cool $tmpl"
        with TemporaryDirectory() as td:
            input_dir = Path(td)

            base_tmpl_path = input_dir / "base.tmpl"
            base_tmpl_path.write_text(template_str)

            result = TemplateRepository.load_from_directory(input_dir)

            assert result.base_template == Template(template_str)
