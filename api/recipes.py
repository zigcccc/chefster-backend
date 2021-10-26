from uuid import UUID
from fastapi import APIRouter, Body, Depends, status
from sqlmodel import Session, select
from typing import List

from dependencies.users import get_current_user_id

from dependencies.db import get_db

from helpers.dictionaries import get_sorted_dict

from models.recipe import Recipe

router = APIRouter(prefix="/recipes")


@router.get("/", response_model=List[Recipe])
async def read_recipes(db: Session = Depends(get_db)):
    return db.exec(select(Recipe)).all()


@router.get('/my', response_model=List[Recipe])
async def read_my_recipes(db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    statement = select(Recipe).where(Recipe.owner_id == user_id)

    return db.exec(statement=statement).all()


@router.post(
    "/",
    response_model=Recipe,
    status_code=status.HTTP_201_CREATED,
)
async def create_recipe(recipe: Recipe, user_id=Depends(get_current_user_id), db: Session = Depends(get_db)):
    recipe_dict = recipe.dict()
    recipe_dict.update({"owner_id": user_id})

    db_recipe = Recipe(**recipe_dict)

    db.add(db_recipe)
    db.commit()

    return db_recipe


@router.get(
    "/{recipe_id}",
    response_model=Recipe,
    response_model_exclude_none=True,
)
async def read_recipe(recipe_id: UUID):
    return {"todo": recipe_id}


@router.put("/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: UUID, recipe: Recipe = Body(..., embed=False)):
    recipe_dict = recipe.dict()
    recipe_dict.update({"id": recipe_id})
    recipe_dict.update({"tags": sorted(recipe.tags)})

    return get_sorted_dict(recipe_dict)
