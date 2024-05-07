from typing import Any


from core.utils import FileManager

file_manager_obj = FileManager(
    users_path="databases/users.json",
    roles_path="databases/roles.json"
)

class UserValidator:
    """Validador de usuario."""

    user: dict[str, Any]

    def __init__(self, user: dict[str, Any]) -> None:
        """Constructor de validador de usuario.

        Args:
            user (dict[str, Any]): Usuario a validar.
        """
        self.user = user
    
    def _email_is_valid(self) -> bool:
        """Validar si email de usuario es valido.

        Para que un email sea considerado como valido no debe existir
        en base de datos, cada uno de los usuarios debe tener un email
        único.

        Returns:
            bool: Si es valido o no email de usuario.
        """
        unique = True
        users = file_manager_obj.get_users()
        for user in users:
            if self.user["email"] == user["email"]:
                unique = False
                break
        return unique
    
    def _age_is_valid(self) -> bool:
        """Validar si edad de usuario es valida.

        Para que la edad del usuario sea considerada como valida debe
        tener más de 18 años.

        Returns:
            bool: Si es valida o no la edad del usuario.
        """
        if self.user["age"] > 18:
            return True
        return False

    def _password_is_valid(self) -> bool:
        """Validar si contraseña de usuario es valida.

        Para que la contraseña del usuario sea considerada como valida
        debe tener una longitud mayor a 8 caracteres y menor a 16
        caracteres.

        Returns:
            bool: Si es valida o no contraseña del usuario.
        """
        if len(self.user["password"]) > 8 and len(self.user["password"]) < 16:
            return True
        return False

    def _roles_are_valid(self) -> bool:
        """Validar si roles de usario son validos.

        Para que los roles de usuario sean considerados como validos
        los nombres de cada uno de los roles debe existir en la base de
        datos (lista de diccionarios) de roles.

        Returns:
            bool: Si son validos o no roles del usuario.
        """
        roles_database = file_manager_obj.get_roles()
        roles_database_list = []
        for role in roles_database:
            roles_database_list.append(role["name"])
        roles_set = set(self.user["roles"])
        roles_database_set = set(roles_database_list)
        
        difference = roles_set - roles_database_set
        if len(difference) > 0 or len(self.user["roles"]) == 0:
            return False
        return True

    def exists_id(self, id_: str) -> bool:
        """Validar si existe ID de usuario.

        Args:
            id_ (str): Id de usuario a buscar.

        Returns:
            bool: Si existe o no ID de usuario.
        """
        users = file_manager_obj.get_users()
        exists = False
        for user in users:
            if id_ == user["id"]:
                exists = True
                break
        return exists
    
    def is_valid(self) -> bool:
        """Validar si usuario es valido.

        Se realizan validaciones de:
        - email
        - edad
        - contraseña
        - roles

        Returns:
            bool: Si usuario es valido o no lo es.
        """
        email_ = self._email_is_valid()
        age_ = self._age_is_valid()
        password_ = self._password_is_valid()
        roles_ = self._roles_are_valid()
        
        if email_ and age_ and password_ and roles_:
            return True
        return False

