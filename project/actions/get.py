from typing import Any
from core.validators import UserValidator

from core.operations import get_users

def get(id: str | None) -> list[dict[str, Any]]:
    obj_user = UserValidator(user={})
    if id:
        if not obj_user.exists_id(id_=id):
            print("NO EXISTE USUARIO A OBTENER")
            return False
    
    return get_users(id_=id)
