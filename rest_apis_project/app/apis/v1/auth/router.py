from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Header
import jwt
from app.apis.v1.auth.types_in import LoginModel
from app.core.v1.operations import Database
from app.settings.v1.settings import SETTINGS
from fastapi import HTTPException


router = APIRouter(tags=["Auth"])


@router.post(
    "/login",
    summary="Iniciar sesión.",
    # response_model=LoginModel,
    status_code=200
)
async def login(data: LoginModel):
    print(data)
    obj_database = Database()
    try:
        user_data = obj_database.login(data=data)
    except Exception as err:
        print(err)
        raise HTTPException(401, detail="Usuario y/o contraseña incorrectos.")

    
    token_data = {
        "email": data.email,
        "roles": user_data.get("roles"),
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=2)
    }
    encoded = jwt.encode(token_data, SETTINGS.GENERAL.HASH_KEY, algorithm="HS512")
    return {"token": encoded}

@router.post(
    "/test",
    summary="Test.",
    status_code=200
)
async def test(token: str = Header(default=None)):
    try:
        data = jwt.decode(token, SETTINGS.GENERAL.HASH_KEY, algorithms=["HS512"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="El token ya expiró")
    except jwt.InvalidSignatureError:
        raise HTTPException(status_code=403, detail="Fallo verificación de firma")
    except jwt.InvalidAlgorithmError:
        raise HTTPException(status_code=403, detail="Algorítmo inválido")
    return {"data": data}
