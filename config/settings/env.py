from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured

env = environ.Env()


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = BASE_DIR / "app"

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    env.read_env(str(BASE_DIR / ".env"))


def env_to_enum(enum_cls: list, value: str) -> None | str:
    for x in enum_cls:
        if x.value == value:
            return x
    message = f"Env value {value!r} could not be found in {enum_cls!r}"
    raise ImproperlyConfigured(message)
