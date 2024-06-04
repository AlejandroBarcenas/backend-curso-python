
from typing import Any

import bcrypt
from bson import ObjectId

from app.apis.v1.auth.types_in import LoginModel
from app.apis.v1.users.types_in import InsertUserModel, UpdateUserModel
from pymongo import MongoClient
from pymongo.collection import Collection
from app.settings.v1.settings import SETTINGS

class Database:

    collection: Collection

    def __init__(self):
        client = MongoClient(SETTINGS.GENERAL.MONGO_CONNECTION_STRING)
        database = client["curso-python"]
        self.collection = database["users"]
    
    def insert_user(self, user: InsertUserModel) -> None:
        """Insertar usuario en base de datos.

        Se le genera un identificador único (uuid) al usuario
        y se agrega a la lista de usuarios (base de datos).

        Args:
            user (dict[str, Any]): Usuario a agregar a base de datos.
        """
        user_dict = user.model_dump()
        result = self.collection.insert_one(user_dict)
        user_dict["id"] = str(result.inserted_id)
        return user_dict

    def update_user(self, user: UpdateUserModel) -> None:
        """Modificar usuario en base de datos.

        Se modifica registro de usuario en lista de usuarios (base de datos).

        Args:
            user (dict[str, Any]): Usuario a modificar en base de datos.
        """
        filter_ = {"_id": ObjectId(user.id)}
        update = {
            "$set": user.model_dump(exclude_none=True, exclude={'id'})
        }

        self.collection.update_one(filter_, update)
        user_modified = self.collection.find_one(filter_)
        user_modified["id"] = str(user_modified['_id'])
        return user_modified

    def delete_user(self, id_: str) -> None:
        """Eliminar usuario de base de datos.

        Args:
            id_ (str): Identificador de usuario a eliminar.
        """
        filter_ = {"_id": ObjectId(id_)}
        self.collection.delete_one(filter_)

    def get_users(self, id_: str | None) -> list[dict[str, Any]]:
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
        users = self.collection.find(filter_)
        users_list = list(users)
        for user in users_list:
            user["id"] = str(user['_id'])
        return users_list

    def login(self, data: LoginModel):
        filter_ = {"email": data.email}
        user_data = self.collection.find_one(
            filter_,
            projection={"roles": 1, "password": 1, "email": 1, "_id": 0}
        )
        if not user_data:
            raise Exception("El usuario no existe")

        hashed = user_data.get("password")
        original_pass = data.password
        hashed_bytes = hashed.encode("utf-8")
        password_bytes = original_pass.encode("utf-8")

        if not bcrypt.checkpw(password_bytes, hashed_bytes):
            raise Exception("Contraseña incorrecta")
        
        return user_data