# Proyecto


## Definición
- Crear usuarios
    - Enviar toda la información (a excepción del ID e insertarla en una "base de datos")
    - Validar contraseñas (8 digitos)
    - Validar email (unico)
    - Validar edad (+18 años)
    - Roles (Roles existentes)
- Modificar usuarios
- Eliminar usuarios
- Obtener usuarios

## Campos de los usuarios
- id (uuid)
- name
- last_name
- age (+18 años)
- email (Campo único)
- password (8 < password < 16)
- roles (los roles tienen que existir)

## Estructura de archivos y carpetas
```text
project/
├── actions/
│   ├── __init__.py
│   ├── delete.py
│   ├── get.py
│   ├── insert.py
│   └── update.py
├── core/
│   ├── __init__.py
│   ├── operations.py
│   └── validators.py
├── databases/
│   ├── __init__.py
│   ├── roles.py
│   └── users.py
└── main.py
```
## Explicación de estructuras y carpetas
- **project/:** Proyecto principal donde desarrollaremos todo el código.
- **main.py:** Archivo principal que ejecutará todas las acciones necesarias.
- **actions/:** Carpeta donde se almacenarán todas las acciones para pruebas.
    - **delete.py:** Archivo de prueba para eliminar usuario.
    - **get.py:** Archivo de prueba para obtener usuario(s).
    - **insert.py:** Archivo de prueba para insertar usuario.
    - **update.py:** Archivo de prueba para modficar usuario.
- **core/:** Carpeta donde se almacenará toda nuestra funcionalidad de la aplicación
    - **operations.py:** En este archivo se meterán todas las funciones para agregar, modificar, eliminar, y visualizar usuarios.
    - **validators.py:** Archivo que contendrá funciones para validación de datos de entrada.
- **databases/:** En esta carpeta se meterán nuestros archivos de simulación de base de datos
    - **roles.py:** Aqui se agregará nuestra base de datos de roles.
    - **users.py:** Aqui se agregará nuestra base de datos de usuarios.


# Detalle de flujos
## Insertar usuario
1. Recibir datos (opcional)
2. Validar datos
    1. Validar si email existe en base de datos.
    2. Validar que la edad sea mayor de 18.
    3. Validar que contraseña sea mayor de 8 dígitos y menor de 16 dígitos.
    4. Validar que los roles existan en base de datos.
3. Si pasa todas las validaciones:
    1. Mandar a llamar método de insertar.
        1. Generar UUID de usuario.
        2. Agregar registro a "base de datos".
4. Sino pasa validaciones:
    1. Imprimir mensaje de error.
5. Fin del flujo

## Modificar usuario
1. Recibir datos (opcional)
2. Validar datos
    1. Validar si email existe en base de datos.
    2. Validar que la edad (opcional) sea mayor de 18.
    3. Validar que los roles (opcional) existan en base de datos.
3. Si pasa todas las validaciones:
    1. Mandar a llamar método de modificar.
        1. Recuperar elemento de usuario.
        2. Modificar registros en "base de datos".
4. Sino pasa validaciones:
    1. Imprimir mensaje de error.
5. Fin del flujo

## Obtener usuario(s)
1. Recibir ID (opcional)
2. Si recibimos ID:
    1. Validar si existe usuario en base de datos.
    2. Si existe:
        1. Mandar a llamar método de busqueda:
            1. Recuperar elemento de usuario.
    3. Sino existe:
        1. Imprimir mensaje de que no existe usuario.
3. Si no recibimos ID:
    1. Mandar a llamar método de busqueda:
        1. Obtener todos los usuarios.
4. Fin del flujo

## Eliminar usuario
1. Recibir ID
2. Validar si existe usuario en base de datos.
    1. Si existe:
        1. Mandar a llamar método de eliminado:
            1. Eliminar elemento de usuario de lista.
    2. Sino existe:
        1. Imprimir mensaje de que no existe usuario.
3. Fin del flujo



### Ejemplos
```python
users = [
    {
        "id": "1234",
        "name": "Alejandro",
        "last_name": "Barcenas Rosas",
        "age": 28,
        "email": "alejandro@email.com",
        "password": "pwd12345",
        "roles": ["ADMIN", "WRITER", "READER"],
    }
]

roles = [
    {
        "id": "1234",
        "name": "ADMIN"
    },
    {
        "id": "12345",
        "name": "WRITER"
    }
    {
        "id": "123456",
        "name": "READER"
    }
]
```