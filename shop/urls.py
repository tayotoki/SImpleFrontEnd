from . import views


urlpatterns = [
    {"url": "/", "view": views.index, "name": "main_page"},
    {"url": "/categories", "view": views.categories, "name": "categories"},
    {"url": "/orders", "view": views.orders, "name": "orders"},
]