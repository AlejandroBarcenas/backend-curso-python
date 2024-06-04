"""Application initialization."""

from app import __DESCRIPTION__, __TITLE__
from app.apis.v1 import app as app_v1
from fastapi import FastAPI

def create_app():
    """Create FatAPI app depending Environment."""
    app = FastAPI(
        title=__TITLE__,
        version="X.X.X",
        description=__DESCRIPTION__,
    )
    app.mount(path="/v1", app=app_v1)
    return app