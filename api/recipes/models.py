from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Set


class Image(BaseModel):
    url: HttpUrl
    name: str


class Recipe(BaseModel):
    title: str = Field(..., title="Recipe title", max_length=140)
    description: Optional[str] = Field(
        None,
        title="Description of the recipe",
        max_length=280
    )
    difficulty: int = Field(
        ...,
        title="The difficulty of this recipe",
        gt=0,
        le=5
    )
    is_vegan: Optional[bool] = Field(
        False,
        title="Is this recipe suitable for vegans"
    )
    tags: Set[str] = Field([], title="Tags for a recipe", max_items=5)
    images: List[Image] = Field([], title="Recipe images", max_items=10)
