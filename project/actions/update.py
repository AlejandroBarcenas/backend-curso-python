from typing import Any
from core.validators import UserValidator
from core.operations import update_user

def update(user: dict[str, Any]):
    
    obj_user = UserValidator(user=user)
    if not obj_user.exists_id(id_=user["id"]):
        print("NO EXISTE USUARIO A MODIFICAR")
        return False
    
    email_ = True
    age_ = True
    roles_ = True
    
    # Validate
    if "email" in user:
        email_ = obj_user._email_is_valid()
    if "age" in user:
        age_ = obj_user._age_is_valid()
    if "roles" in user:
        roles_ = obj_user._roles_are_valid()
    
    if email_ and age_ and roles_:
        print("SI ES UN USUARIO VALIDO")
        update_user(user)
    else:
        print("NO ES UN USUARIO VALIDO")
