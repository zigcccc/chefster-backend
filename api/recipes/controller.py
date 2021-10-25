from fastapi import APIRouter, Body, HTTPException, status
from random import randint

from helpers.dictionaries import get_sorted_dict

from .fixtures import recipes
from .models import Recipe


router = APIRouter(prefix="/recipes")


@router.get("/",)
def read_recipes():
    return {"Hello": "World"}


@router.post("/",)
async def create_recipe(recipe: Recipe):
    recipe_dict = recipe.dict()
    recipe_dict.update({"rating": randint(1, 10)})

    return recipe_dict


@router.get(
    "/{recipe_id}",
    response_model=Recipe,
    response_model_exclude_none=True,
)
async def read_recipe(recipe_id: str):
    if recipe_id not in recipes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No recipe found for id {recipe_id}"
        )

    return recipes[recipe_id]


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: Recipe = Body(..., embed=True)):
    recipe_dict = recipe.dict()
    recipe_dict.update({"id": recipe_id})
    recipe_dict.update({"tags": sorted(recipe.tags)})

    return get_sorted_dict(recipe_dict)
