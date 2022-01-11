import uvicorn
from fastapi import FastAPI

from core.config import api_settings
from core.event_handlers import start_app_handler, stop_app_handler
from routes.router import api_router


def app_factory() -> FastAPI:
    """
    FastAPI factory pattern
    Returns:
        FastAPI: Our app
    """
    app = FastAPI(title=api_settings.APP_NAME, version=api_settings.VERSION, debug=api_settings.DEBUG_MODE)
    app.include_router(api_router, prefix=api_settings.API_PREFIX)
    app.add_event_handler("startup", start_app_handler(app))
    app.add_event_handler("shutdown", stop_app_handler(app))
    
    return app

app = app_factory()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=api_settings.HOST,
        port=api_settings.PORT,
        reload=api_settings.DEBUG_MODE,
    )