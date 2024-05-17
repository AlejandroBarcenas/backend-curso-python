from bson import ObjectId
from fastapi import FastAPI
from models import InsertUserModel, UpdateUserModel, DeleteUserModel, UserModelResponse, GetUsersModelResponse
from core.operations import Database
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

DESCRIPTION = """
Esta REST API es una de las clases del curso de **Python**.
Considerará los siguientes temas:
- Pydantic
- MongoDB
- FastAPI

"""

app = FastAPI(
    title="REST API - Curso Python",
    description=DESCRIPTION,
    version="1.0.0"
)

TAG_USER = ["Users"]

@app.post(
    "/user",
    tags=TAG_USER,
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

@app.put(
    "/user",
    tags=TAG_USER,
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

@app.delete(
    "/user",
    tags=TAG_USER,
    summary="Eliminar usuario.",
    status_code=204
)
async def delete_user(data: DeleteUserModel):
    obj_database = Database()
    obj_database.delete_user(id_=data.id)
    return {}

@app.get(
    "/user",
    tags=TAG_USER,
    summary="Obtener todos los usuarios.",
    response_model=GetUsersModelResponse,
)
async def get_users():
    obj_database = Database()
    users = obj_database.get_users(id_=None)
    return {"users": users}

@app.get(
    "/user/{user_id}",
    tags=TAG_USER,
    summary="Obtener usuario por ID.",
    response_model=GetUsersModelResponse,
)
async def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(409, detail="El ID de usuario no es valido.")
    obj_database = Database()
    users = obj_database.get_users(id_=user_id)
    return {"users": users}
