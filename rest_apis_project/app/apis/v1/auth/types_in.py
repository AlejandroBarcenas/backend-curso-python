from pydantic import BaseModel, Field


class LoginModel(BaseModel):

    email: str = Field(
        ...,
        title="Email",
        description="Email del usuario",
        examples=["user@email.com"]
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=16,
        title="Contraseña",
        description="Contraseña del usuario",
        examples=["pwd12345"]
    )
