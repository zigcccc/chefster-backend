from fastapi import APIRouter

from enums.tags import PathTags

from .recipes import router as recipesRouter

api_router = APIRouter(prefix="/api")
api_router.include_router(recipesRouter, tags=[PathTags.RECIPES])
