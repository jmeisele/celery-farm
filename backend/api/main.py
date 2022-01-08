import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.event_handlers import start_app_handler, stop_app_handler
from routes.router import api_router


def app_factory() -> FastAPI:
    """
    FastAPI factory pattern
    Returns:
        FastAPI: Our app
    """
    app = FastAPI(title=settings.APP_NAME, version=settings.VERSION, debug=settings.DEBUG_MODE)
    app.include_router(api_router, prefix=settings.API_PREFIX)
    app.add_event_handler("startup", start_app_handler(app))
    app.add_event_handler("shutdown", stop_app_handler(app))
    
    return app

app = app_factory()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG_MODE,
    )