from databases.roles import roles as roles_database
from databases.users import users


def email_is_valid(email: str) -> bool:
    unique = True
    for user in users:
        if email == user["email"]:
            unique = False
            break
    return unique

def age_is_valid(age: int) -> bool:
    if age > 18:
        return True
    return False

def password_is_valid(password: str) -> bool:
    if len(password) > 8 and len(password) < 16:
        return True
    return False

def roles_are_valid(roles: list[str]) -> bool:
    roles_database_list = []
    for role in roles_database:
        roles_database_list.append(role["name"])
    roles_set = set(roles)
    roles_database_set = set(roles_database_list)
    
    difference = roles_set - roles_database_set
    if len(difference) > 0 or len(roles) == 0:
        return False
    return True



    

