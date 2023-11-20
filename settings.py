from pathlib import Path

HOST_NAME = "localhost"
PORT = 8000

BASE_DIR = Path(__file__).resolve().parent
MAIN_TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_URL = "/static"  # Пока что не используется.
PAGE_404_FILE = MAIN_TEMPLATES_DIR / "404.html"

INSTALLED_APPS = [
    "shop",
]
