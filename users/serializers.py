from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Recipe Model Serializer
    """

    class Meta:
        model = User
        fields = ["id", "username", "is_active", "date_joined"]
