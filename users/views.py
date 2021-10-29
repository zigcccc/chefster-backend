from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from constants.http import HttpMethod

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    User View Set
    """

    queryset = User.objects.all().filter(is_superuser__exact=False)
    serializer_class = UserSerializer

    @action(detail=False, methods=[HttpMethod.GET], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)

        return Response(serializer.data)
