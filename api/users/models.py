from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional


class UserModel(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_admin: bool = False


class UserInDB(UserModel):
    hashed_password: str
