from app.apis.v1.users.types_in import BaseUserModel
from pydantic import BaseModel, Field


class UserModelResponse(BaseUserModel):
    """Insert User base model response."""
    id: str = Field(
        ...,
        title="Identificador",
        description="Identificador del usuario",
        examples=["664448aeef147454698ef561"]
    )


class GetUsersModelResponse(BaseModel):
    users: list[UserModelResponse]
