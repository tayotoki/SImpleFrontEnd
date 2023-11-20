from template_engine.engine import ShopTemplateEngine
from .models import Item, Category, Order, FAQ


engine = ShopTemplateEngine()


def index() -> str:
    context = {
        "items": Item.generate_samples()
    }

    return engine.render(template_name="main_page.html", context=context)


def categories() -> str:
    context = {
        "items": Category.generate_samples()
    }

    return engine.render(template_name="categories.html", context=context)


def orders() -> str:
    context = {
        "items": Order.generate_samples()
    }

    return engine.render(template_name="orders.html", context=context)


def faq() -> str:
    context = {
        "items": FAQ.get_samples()
    }

    return engine.render(template_name="faq.html", context=context)
