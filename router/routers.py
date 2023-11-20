import importlib
from collections.abc import Callable
from types import ModuleType
import typing as tp

from settings import INSTALLED_APPS


class URLResolver:
    @classmethod
    def get_controller(cls, path: str) -> tp.Optional[Callable[..., str]]:
        for app in INSTALLED_APPS:
            try:
                module: ModuleType = importlib.import_module(name=".urls", package=app)
            except (ImportError, ModuleNotFoundError) as e:
                print(f"{e}. class {cls.__name__} method get_controller. Package {app}")
            else:
                for urlpattern in module.urlpatterns:  # noqa
                    if path == urlpattern.get("url"):
                        return urlpattern["view"]
