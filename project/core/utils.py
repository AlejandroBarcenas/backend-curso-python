import json
from typing import Any

class FileManager:

    users_path: str
    roles_path: str

    def __init__(self, users_path: str, roles_path: str) -> None:
        self.users_path = users_path
        self.roles_path = roles_path
    
    def get_users(self) -> list[dict[str, Any]]:
        with open(self.users_path, "r", encoding="utf-8") as file:
            content = file.read()
        users = json.loads(content)
        return users
    
    def get_roles(self) -> list[dict[str, Any]]:
        with open(self.roles_path, "r", encoding="utf-8") as file:
            content = file.read()
        roles = json.loads(content)
        return roles
    
    def set_users(self, users: list[dict[str, Any]]) -> bool:
        content = json.dumps(users)
        with open(self.users_path, "w", encoding="utf-8") as file:
            file.write(content)
        return True
    
    def set_roles(self, roles: list[dict[str, Any]]) -> bool:
        content = json.dumps(roles)
        with open(self.roles_path, "w", encoding="utf-8") as file:
            file.write(content)
        return True
