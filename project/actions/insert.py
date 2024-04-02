from typing import Any
from core.validators import (
    age_is_valid,
    email_is_valid,
    password_is_valid,
    roles_are_valid
)
from core.operations import insert_user

def insert(user: dict[str, Any]):
    # Validate
    email_ = email_is_valid(email=user["email"])
    age_ = age_is_valid(age=user["age"])
    password_ = password_is_valid(password=user["password"])
    roles_ = roles_are_valid(roles=user["roles"])
    
    if email_ and age_ and password_ and roles_:
        print("SI ES UN USUARIO VALIDO")
        insert_user(user)
    else:
        print("NO ES UN USUARIO VALIDO")
