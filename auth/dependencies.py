from fastapi import Depends, HTTPException, status

from .schemas import token_auth_schema
from .utils import VerifyToken


async def get_token(token: str = Depends(token_auth_schema)) -> str:
    """
    Basic "is user authenticated" auth dependency. Raises an HTTPException if
    passed token is not valid. Grabs the token from token_auth_schema as a
    dependency.
    """
    result = VerifyToken(token.credentials).verify()

    if result.get("status") == "error":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result)

    return token.credentials
