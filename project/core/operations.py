

from typing import Any
from uuid import uuid4

from databases.users import users


def insert_user(user: dict[str, Any]):
    print(f"OLD USERS: {users}")
    user["id"] = str(uuid4())
    users.append(user)

    print(f"\n\n NEW USERS: {users}")

