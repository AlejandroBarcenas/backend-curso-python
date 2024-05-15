from core.operations import insert_user, update_user, delete_user, get_users
from actions.get import get
from models import User


# INSERTAR
# user = {
#     "name": "Alejandro",
#     "last_name": "Barcenas Rosas",
#     "age": 20,
#     "email": "alejandro1@email.com",
#     "password": "pwd123456",
#     "roles": ["ADMIN"]
# }
# obj_user = User(**user)
# insert_user(user=obj_user)


# MODIFICAR
# user = {
#     "id": "664448aeef147454698ef561",
#     "age": 20,
#     "email": "alejandro_nuevo@email.com",
#     "roles": ["WRITER", "READER"]
# }
# user_obj = User(**user)
# update_user(user=user_obj)


# ELIMINAR
# user = {"id": "6644491038a097313d06a13a"}
# user_obj = User(**user)
# delete_user(id_=user_obj.id)


# OBTENER

user = {"id": "664448aeef147454698ef561"}
user_obj = User(**user)

# users = get_users(id_=user_obj.id)
# print(f"\nUSERS: {users}\n")


# all_users = get_users(id_=None)
# print(f"\nALL_USERS: {all_users}\n")
