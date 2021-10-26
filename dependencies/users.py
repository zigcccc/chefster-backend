from fastapi import Depends, HTTPException, status
from typing import Union

from auth import dependencies, utils


def get_current_user_id(token: str = Depends(dependencies.get_token)) -> Union[str, None]:
    result = utils.VerifyToken(token).verify()

    if result.get("status") == "error":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=result)

    return result["sub"]
