import os
import sys
from pathlib import Path
from typing import Any

from django.core.asgi import get_asgi_application

from config.websocket import websocket_application

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "app"))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.local")

django_application = get_asgi_application()


async def application(scope: Any, receive: Any, send: Any) -> None:
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_application(scope, receive, send)
    else:
        msg = f"Unknown scope type {scope['type']}"
        raise NotImplementedError(msg)
