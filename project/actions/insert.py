from typing import Any
from core.validators import UserValidator
from core.operations import insert_user

def insert(user: dict[str, Any]):
    """Insertar usuario.

    Args:
        user (dict[str, Any]): Usuario a insertar.
    """
    obj_user = UserValidator(user=user)
    if obj_user.is_valid():
        print("SI ES UN USUARIO VALIDO")
        insert_user(user)
    else:
        print("NO ES UN USUARIO VALIDO")
