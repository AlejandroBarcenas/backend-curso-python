

import os
from typing import Any
from uuid import uuid4

from core.utils import FileManager


file_manager_obj = FileManager(
    users_path=f"{os.getcwd()}/databases/users.json",
    roles_path=f"{os.getcwd()}/databases/roles.json"
)

def insert_user(user: dict[str, Any]) -> None:
    """Insertar usuario en base de datos.

    Se le genera un identificador único (uuid) al usuario
    y se agrega a la lista de usuarios (base de datos).

    Args:
        user (dict[str, Any]): Usuario a agregar a base de datos.
    """
    users = file_manager_obj.get_users()
    print(f"OLD USERS: {users}")
    user["id"] = str(uuid4())
    users.append(user)
    print(f"\n\n NEW USERS: {users}")
    file_manager_obj.set_users(users)

def update_user(user: dict[str, Any]) -> None:
    """Modificar usuario en base de datos.

    Se modifica registro de usuario en lista de usuarios (base de datos).

    Args:
        user (dict[str, Any]): Usuario a modificar en base de datos.
    """
    users = file_manager_obj.get_users()
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
    file_manager_obj.set_users(users)

def delete_user(id_: str) -> None:
    """Eliminar usuario de base de datos.

    Args:
        id_ (str): Identificador de usuario a eliminar.
    """
    users = file_manager_obj.get_users()
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
    file_manager_obj.set_users(users)

def get_users(id_: str | None) -> list[dict[str, Any]]:
    """Obtener usuario(s) de base de datos.

    Si se envía un identificador de usuario se devolverá el usuario
    solicitado en una lista con un solo elemento, en caso de no mandar
    un identificador se devolverán todos los usuarios de la base de datos.

    Args:
        id_ (str | None): Identificador de usuario a recuperar.

    Returns:
        list[dict[str, Any]]: Lista de usuario(s) obtenidos de base de datos.
    """
    users = file_manager_obj.get_users()
    if id_:
        # Find user
        index = 0
        for index, user_database in enumerate(users):
            if id_ == user_database["id"]:
                index = index
                break
        return [users[index]]
    return users
