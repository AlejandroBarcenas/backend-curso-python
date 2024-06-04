"""Router version 1."""
from app import __TITLE__
from app.apis.v1.users.router import router as router_users
from app.apis.v1.auth.router import router as router_auth
from fastapi import FastAPI

description = """
### Sections
- **Auth** Manage Authentication.
- **Users** Manage Users.

For more details you can go to [General Documentation](/docs).
"""

app = FastAPI(
    title=__TITLE__,
    version="1.0.0",
    description=description,
)

app.include_router(router_auth)
app.include_router(router_users)