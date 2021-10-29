from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Model Serializer
    """

    class Meta:
        model = User
        fields = ["id", "username", "is_active", "date_joined", "recipes_count"]
