from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends

from dependencies.users import get_current_user

from .models import UserModel

router = APIRouter(prefix="/users")


@router.post(
    "/",
    response_model=UserModel,
    response_model_exclude={"password"},
    response_model_exclude_none=True,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: UserModel):
    if not user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong username or password"
        )

    return user


@router.get('/me')
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user
