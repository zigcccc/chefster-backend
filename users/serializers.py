from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Recipe Model Serializer
    """

    class Meta:
        model = User
        fields = ["id", "username"]
