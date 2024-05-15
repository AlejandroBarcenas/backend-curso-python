
from typing import Any

from bson import ObjectId

from models import User
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
database = client["curso-python"]
collection = database["users"]

def insert_user(user: User) -> None:
    """Insertar usuario en base de datos.

    Se le genera un identificador único (uuid) al usuario
    y se agrega a la lista de usuarios (base de datos).

    Args:
        user (dict[str, Any]): Usuario a agregar a base de datos.
    """
    collection.insert_one(user.model_dump(exclude_none=True))

def update_user(user: User) -> None:
    """Modificar usuario en base de datos.

    Se modifica registro de usuario en lista de usuarios (base de datos).

    Args:
        user (dict[str, Any]): Usuario a modificar en base de datos.
    """
    filter_ = {"_id": ObjectId(user.id)}
    update = {
        "$set": user.model_dump(exclude_none=True, exclude={'id'})
    }
    collection.update_one(filter_, update)

def delete_user(id_: str) -> None:
    """Eliminar usuario de base de datos.

    Args:
        id_ (str): Identificador de usuario a eliminar.
    """
    filter_ = {"_id": ObjectId(id_)}
    collection.delete_one(filter_)

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
    filter_ = {}
    if id_:
        filter_ = {"_id": ObjectId(id_)}
    users = collection.find(filter_)
    return list(users)
