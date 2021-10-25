from pydantic import BaseModel, networks
from typing import Optional


class UserModel(BaseModel):
    username: str
    email: networks.EmailStr
    password: str
    full_name: Optional[str] = None
    is_admin: bool = False
