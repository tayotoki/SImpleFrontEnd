from .engine import FileSystemTemplateEngine

common_template = FileSystemTemplateEngine()


def get_404_template() -> bytes:
    return bytes(common_template.render("404.html"), "utf-8")
