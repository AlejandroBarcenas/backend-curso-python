from core.validators import UserValidator

from core.operations import delete_user

def delete(id: str) -> bool | None:
    """Eliminar usuario.

    Args:
        id (str): Identificador de usuario a eliminar.

    Returns:
        bool | None: False si no existe usuario a eliminar.
    """
    obj_user = UserValidator(user={})
    if not obj_user.exists_id(id_=id):
        print("NO EXISTE USUARIO A ELIMINAR")
        return False
    delete_user(id_=id)
