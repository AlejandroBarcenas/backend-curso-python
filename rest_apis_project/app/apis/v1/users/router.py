"""Router users APIS definition."""

from bson import ObjectId
from fastapi import APIRouter
from app.apis.v1.users.types_out import UserModelResponse, GetUsersModelResponse
from app.apis.v1.users.types_in import InsertUserModel, UpdateUserModel, DeleteUserModel
from app.core.v1.operations import Database
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

router = APIRouter(tags=["Users"])

@router.post(
    "/user",
    summary="Agregar nuevo usuario.",
    response_model=UserModelResponse,
    status_code=201
)
async def insert_user(data: InsertUserModel):
    obj_database = Database()
    try:
        user_inserted = obj_database.insert_user(user=data)
    except DuplicateKeyError:
        raise HTTPException(409, detail="El usuario ya existe en base de datos.")
    return user_inserted

@router.put(
    "/user",
    summary="Modificar usuario existente.",
    response_model=UserModelResponse
)
async def update_user(data: UpdateUserModel):
    obj_database = Database()
    try:
        user_modified = obj_database.update_user(user=data)
    except DuplicateKeyError:
        raise HTTPException(409, detail="El usuario ya existe en base de datos.")
    return user_modified

@router.delete(
    "/user",
    summary="Eliminar usuario.",
    status_code=204
)
async def delete_user(data: DeleteUserModel):
    obj_database = Database()
    obj_database.delete_user(id_=data.id)
    return {}

@router.get(
    "/user",
    summary="Obtener todos los usuarios.",
    response_model=GetUsersModelResponse,
)
async def get_users():
    obj_database = Database()
    users = obj_database.get_users(id_=None)
    return {"users": users}

@router.get(
    "/user/{user_id}",
    summary="Obtener usuario por ID.",
    response_model=GetUsersModelResponse,
)
async def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(409, detail="El ID de usuario no es valido.")
    obj_database = Database()
    users = obj_database.get_users(id_=user_id)
    return {"users": users}
