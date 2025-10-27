from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.events import create_start_app_handler, create_stop_app_handler # type: ignore

def get_application() -> FastAPI:

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler( # type: ignore
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler( # type: ignore
        "shutdown",
        create_stop_app_handler(application),
    )


    return application


app = get_application()