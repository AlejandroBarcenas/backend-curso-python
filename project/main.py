from actions.insert import insert


# INSERTAR
user = {
    "name": "Alejandro",
    "last_name": "Barcenas Rosas",
    "age": 20,
    "email": "alejandro1@email.com",
    "password": "pwd123456",
    "roles": ["ADMIN"]
}

insert(user=user)

# MODIFICAR
user = {
    "id": "1234",
    "age": 20,
    "email": "alejandro1@email.com",
    "roles": ["ADMIN"]
}

# update(user=user)

# ELIMINAR
user = {
    "id": "1234"
}

# delete(user=user)

# OBTENER
user = {"id": None}

# get(user=user)
