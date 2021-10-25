from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from random import randint
from typing import Dict
from uuid import UUID, uuid4

from helpers.dictionaries import get_sorted_dict

from .models import Recipe


router = APIRouter(prefix="/recipes")

fake_db: Dict[UUID, Recipe] = {}


@router.get("/",)
async def read_recipes():
    return list(fake_db.values())


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_recipe(recipe: Recipe):
    recipe_dict = recipe.dict()
    recipe_dict.update({"rating": randint(1, 10)})

    id = uuid4()
    recipe_dict.update({"id": id})

    fake_db[id] = jsonable_encoder(recipe_dict)

    return recipe_dict


@router.get(
    "/{recipe_id}",
    response_model=Recipe,
    response_model_exclude_none=True,
)
async def read_recipe(recipe_id: UUID):
    if recipe_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No recipe found for id {recipe_id}"
        )

    return fake_db[recipe_id]


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: UUID, recipe: Recipe = Body(..., embed=False)):
    recipe_dict = recipe.dict()
    recipe_dict.update({"id": recipe_id})
    recipe_dict.update({"tags": sorted(recipe.tags)})

    return get_sorted_dict(recipe_dict)
