

from typing import Any
from uuid import uuid4

from databases.users import users


def insert_user(user: dict[str, Any]):
    print(f"OLD USERS: {users}")
    user["id"] = str(uuid4())
    users.append(user)

    print(f"\n\n NEW USERS: {users}")

def update_user(user: dict[str, Any]) -> bool:
    
    print(f"OLD USERS: {users}")
    # Find user
    index = 0
    for index, user_database in enumerate(users):
        if user["id"] == user_database["id"]:
            index = index
            break
    # Update user
    for key in user:
        print(key)
        users[index][key] = user[key]
    print(f"\n\n NEW USERS: {users}")


def delete_user(id_: str):
    print(f"OLD USERS: {users}")
    # Find user
    index = 0
    for index, user_database in enumerate(users):
        if id_ == user_database["id"]:
            index = index
            break
    # Update user
    users.pop(index)
    print(f"\n\n NEW USERS: {users}")

def get_users(id_: str | None) -> list[dict[str, Any]]:
    if id_:
        # Find user
        index = 0
        for index, user_database in enumerate(users):
            if id_ == user_database["id"]:
                index = index
                break
        return [users[index]]
    return users
