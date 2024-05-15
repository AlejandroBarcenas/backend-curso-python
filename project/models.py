from typing import Literal, Optional
from bson import ObjectId
from pydantic import BaseModel, Field, field_validator
from pymongo import MongoClient


class User(BaseModel):
    """User base model."""

    id: Optional[str] = Field(None) 
    name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    age: Optional[int] = Field(None, ge=18)
    password: Optional[str] = Field(None, min_length=8, max_length=16)
    roles: Optional[list[Literal["ADMIN", "WRITER", "READER"]]] = Field(None)

    @field_validator('email', mode='after')
    @classmethod
    def validate_email(cls, value_):
        client = MongoClient("mongodb://localhost:27017")
        database = client["curso-python"]
        collection = database["users"]
        count = collection.count_documents({"email": value_})
        if count > 0:
            raise ValueError("Duplicate User")

        return value_
    
    @field_validator('id', mode='after')
    @classmethod
    def validate_object_id(cls, value_):
        if not ObjectId.is_valid(value_):
            raise ValueError("Invalid ObjectId")
        return value_
    

