from rest_framework import serializers

from constants import serialization
from helpers.serializations import mixins

from users.serializers import UserSerializer

from .models import Recipe


class RecipeSerializer(mixins.CreatorFieldFromRequestUserMixin, serializers.ModelSerializer):
    """
    Recipe Model Serializer
    """

    included_serializers = {"creator": UserSerializer}

    class Meta:
        model = Recipe
        fields = [*serialization.common_fields, "title", "description", "creator"]

    class JSONAPIMeta:
        included_resources = ["creator"]
