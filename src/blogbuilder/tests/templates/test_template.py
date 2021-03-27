import pytest
from unittest import TestCase

from blogbuilder.templates.template import MissingTemplateValueError, Template


class TemplateTest(TestCase):
    def test_render_uses_the_template(self) -> None:
        """
        given a template with a template string
        and no values to interpolate
        it renders the template string as is
        """
        basic_template_str = "sup yo"

        template = Template(basic_template_str)
        result = template.render({})

        assert basic_template_str == result

    def test_render_interpolates_value(self) -> None:
        """
        given a template with a template string
        and a value to interpolate
        it interpolates the value into the string
        """
        basic_template_str = "sup $name"

        template = Template(basic_template_str)
        result = template.render({"name": "terry"})

        assert "sup terry" == result

    def test_render_missing_value(self) -> None:
        """
        given insufficient values to populate the template string
        it raises an error
        """
        template = Template("$nope")
        with pytest.raises(
            MissingTemplateValueError, match="Missing template value 'nope'"
        ):
            template.render({})
