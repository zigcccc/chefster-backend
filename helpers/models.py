from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    """
    Base Model
    - sets the ID field to be UUID
    - sets the created field
    - sets the modified field
    """
    id = models.UUIDField(db_index=True, default=uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
