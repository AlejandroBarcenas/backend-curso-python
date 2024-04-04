from core.validators import UserValidator

from core.operations import delete_user

def delete(id: str):
    obj_user = UserValidator(user={})
    if not obj_user.exists_id(id_=id):
        print("NO EXISTE USUARIO A ELIMINAR")
        return False
    delete_user(id_=id)
