"""Template rendering for dummies."""
from jinja2 import Environment
from jinja2 import FileSystemLoader


class Renderer:

    """A simple template renderer."""

    def __init__(self, template_directory, site_globals):
        """Make a new template renderer."""
        self.env = Environment(loader=FileSystemLoader(template_directory))
        self.site_globals = site_globals

    def __call__(self, page):
        """Render something."""
        template = self.env.get_template(page['template'])
        return template.render(page=page, **self.site_globals)

    @property
    def filters(self):
        """Expose the jinja filters for easy custom filters."""
        return self.env.filters
