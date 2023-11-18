from template_engine.engine import ShopTemplateEngine
from .models import Item


engine = ShopTemplateEngine()


def index() -> str:
    context = {
        "items": Item.generate_samples()
    }

    return engine.render(template_name="main_page.html", context=context)
