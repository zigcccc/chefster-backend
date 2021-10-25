from fastapi import APIRouter

from enums.tags import PathTags

from .auth.controller import router as authRouter
from .recipes.controller import router as recipesRouter
from .users.controller import router as usersRouter

api_router = APIRouter(prefix="/api")
api_router.include_router(authRouter, tags=[PathTags.AUTH])
api_router.include_router(recipesRouter, tags=[PathTags.RECIPES])
api_router.include_router(usersRouter, tags=[PathTags.USERS])
