from typing import Any
from databases.roles import roles as roles_database
from databases.users import users


class UserValidator:

    user: dict[str, Any]

    def __init__(self, user: dict[str, Any]) -> None:
        self.user = user
    
    def _email_is_valid(self) -> bool:
        unique = True
        for user in users:
            if self.user["email"] == user["email"]:
                unique = False
                break
        return unique
    
    def _age_is_valid(self) -> bool:
        if self.user["age"] > 18:
            return True
        return False

    def _password_is_valid(self) -> bool:
        if len(self.user["password"]) > 8 and len(self.user["password"]) < 16:
            return True
        return False

    def _roles_are_valid(self) -> bool:
        roles_database_list = []
        for role in roles_database:
            roles_database_list.append(role["name"])
        roles_set = set(self.user["roles"])
        roles_database_set = set(roles_database_list)
        
        difference = roles_set - roles_database_set
        if len(difference) > 0 or len(self.user["roles"]) == 0:
            return False
        return True

    def exists_id(self, id_: str) -> bool:
        exists = False
        for user in users:
            if id_ == user["id"]:
                exists = True
                break
        return exists
    
    def is_valid(self):
        email_ = self._email_is_valid()
        age_ = self._age_is_valid()
        password_ = self._password_is_valid()
        roles_ = self._roles_are_valid()
        
        if email_ and age_ and password_ and roles_:
            return True
        return False

