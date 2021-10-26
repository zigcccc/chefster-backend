from sqlalchemy import Column, Integer, String, Boolean
from pydantic import BaseModel, HttpUrl

from db.database import Base


class Image(BaseModel):
    url: HttpUrl
    name: str


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String, nullable=True)
    difficulty = Column(Integer)
    is_vegan = Column(Boolean, default=False)
