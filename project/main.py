from actions.insert import insert
from actions.update import update
from actions.delete import delete
from actions.get import get


# INSERTAR

# user = {
#     "name": "Alejandro",
#     "last_name": "Barcenas Rosas",
#     "age": 20,
#     "email": "alejandro1@email.com",
#     "password": "pwd123456",
#     "roles": ["ADMIN"]
# }
# insert(user=user)


# MODIFICAR

# user = {
#     "id": "1234",
#     "age": 20,
#     "email": "alejandro_nuevo@email.com",
#     "roles": ["WRITER"]
# }
# update(user)


# ELIMINAR

# user = {
#     "id": "1234"
# }
# delete(id=user["id"])


# OBTENER

# user = {"id": "1234"}
# users = get(id=user["id"])
# print(f"\nUSERS: {users}\n")
# all_users = get(id=None)
# print(f"\nALL_USERS: {all_users}\n")
