from . import views


urlpatterns = [
    {"url": "/", "view": views.index, "name": "main_page"},
]