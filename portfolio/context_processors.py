# portfolio/context_processors.py
from .version import get_version


def app_version(request):
    return {"APP_VERSION": get_version()}
