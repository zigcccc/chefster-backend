from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field


class Recipe(SQLModel, table=True):
    id: Optional[UUID] = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    title: str = Field(nullable=False)
    description: Optional[str] = Field(default=None)
    owner_id: Optional[str] = Field(nullable=False)
