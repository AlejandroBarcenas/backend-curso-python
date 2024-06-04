from typing import Literal, Optional
import bcrypt
from bson import ObjectId
from pydantic import BaseModel, Field, field_validator


class BaseUserModel(BaseModel):

    name: str = Field(
        ...,
        title="Nombre",
        description="Nombre del usuario",
        examples=["Juan"]
    )
    last_name: str = Field(
        ...,
        title="Apellidos",
        description="Apellidos del usuario",
        examples=["Lopez Pérez"]
    )
    email: str = Field(
        ...,
        title="Email",
        description="Email del usuario",
        examples=["user@email.com"]
    )
    age: int = Field(
        ...,
        ge=18,
        title="Edad",
        description="Edad del usuario",
        examples=[24]
    )
    roles: list[Literal["ADMIN", "WRITER", "READER"]] = Field(
        ...,
        title="Roles",
        description="Roles del usuario",
        examples=[["ADMIN", "WRITER", "READER"]]
    )


class InsertUserModel(BaseUserModel):
    """Insert User base model."""
    
    password: str = Field(
        ...,
        min_length=8,
        max_length=16,
        title="Contraseña",
        description="Contraseña del usuario",
        examples=["pwd12345"]
    )

    @field_validator('password', mode='after')
    @classmethod
    def hash_password(cls, value_: str):
        password_bytes = value_.encode('utf-8')
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt(14))
        return hashed_bytes.decode('utf-8')


class UpdateUserModel(BaseModel):
    """Update User base model."""

    id: str = Field(
        ...,
        title="Identificador",
        description="Identificador del usuario",
        examples=["664448aeef147454698ef561"]
    )
    name: Optional[str] = Field(
        None,
        title="Nombre",
        description="Nombre del usuario",
        examples=["Juan"]
    )
    last_name: Optional[str] = Field(
        None,
        title="Apellidos",
        description="Apellidos del usuario",
        examples=["Lopez Pérez"]
    )
    email: Optional[str] = Field(
        None,
        title="Email",
        description="Email del usuario",
        examples=["user@email.com"]
    )
    age: Optional[int] = Field(
        None,
        ge=18,
        title="Edad",
        description="Edad del usuario",
        examples=[24]
    )
    password: Optional[str] = Field(
        None,
        min_length=8,
        max_length=16,
        title="Contraseña",
        description="Contraseña del usuario",
        examples=["pwd12345"]
    )
    roles: Optional[list[Literal["ADMIN", "WRITER", "READER"]]] = Field(
        None,
        title="Roles",
        description="Roles del usuario",
        examples=[["ADMIN", "WRITER", "READER"]]
    )
    
    @field_validator('id', mode='after')
    @classmethod
    def validate_object_id(cls, value_):
        if not ObjectId.is_valid(value_):
            raise ValueError("Invalid ObjectId")
        return value_
    
    @field_validator('password', mode='after')
    @classmethod
    def hash_password(cls, value_: str):
        password_bytes = value_.encode('utf-8')
        hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt(14))
        return hashed_bytes.decode('utf-8')
    

class DeleteUserModel(BaseModel):
    """Delete User base model."""

    id: str = Field(
        ...,
        title="Identificador",
        description="Identificador del usuario",
        examples=["664448aeef147454698ef561"]
    )

    @field_validator('id', mode='after')
    @classmethod
    def validate_object_id(cls, value_):
        if not ObjectId.is_valid(value_):
            raise ValueError("Invalid ObjectId")
        return value_
