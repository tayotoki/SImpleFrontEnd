import jinja2
import abc
import typing as tp

import settings


class FileSystemTemplateEngine:
    def __init__(self):
        self.env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(searchpath=settings.MAIN_TEMPLATES_DIR),
            autoescape=True
        )

    def _get_template(self, name: str) -> jinja2.Template:
        return self.env.get_template(name=name)

    def render(self, template_name: str) -> str:
        template = self._get_template(name=template_name)

        return template.render()


class AppTemplateEngine:
    def __init_subclass__(cls, /, package_name: tp.Optional[str] = None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.package_name = package_name

    def __init__(self):
        self.env = jinja2.Environment(
            loader=jinja2.PackageLoader(package_name=self.package_name),
            autoescape=True
        )

    def _get_template(self, name: str) -> jinja2.Template:
        return self.env.get_template(name=name)

    def render(self, template_name: str, context: dict[str, tp.Any]) -> str:
        template = self._get_template(name=template_name)

        return template.render(**context)


class ShopTemplateEngine(AppTemplateEngine, package_name="shop"):
    pass
