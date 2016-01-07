"""Template rendering for dummies."""
from jinja2 import Environment
from jinja2 import FileSystemLoader


class Renderer:
    """A simple template renderer."""

    def __init__(self, template_directory):
        """Make a new template renderer."""
        self.env = Environment(loader=FileSystemLoader(template_directory))

    def __call__(self, page, template_name, **extras):
        """Render something."""
        template = self.env.get_template(template_name)
        return template.render(page=page, **extras)

    @property
    def filters(self):
        """Expose the jinja filters for easy custom filters."""
        return self.env.filters

    @property
    def globals(self):
        """Expose the jinja globals for easy extension."""
        return self.env.globals

    @property
    def tests(self):
        """Expose the jinja tests for easy extention."""
        return self.env.tests
