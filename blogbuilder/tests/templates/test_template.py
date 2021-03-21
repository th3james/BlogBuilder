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
