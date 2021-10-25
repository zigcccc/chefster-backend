from fastapi import APIRouter

from enums.tags import PathTags

from .recipes.controller import router as recipesRouter
from .users.controller import router as usersRouter

api_router = APIRouter(prefix="/api")
api_router.include_router(recipesRouter, tags=[PathTags.USERS])
api_router.include_router(usersRouter, tags=[PathTags.RECIPES])
