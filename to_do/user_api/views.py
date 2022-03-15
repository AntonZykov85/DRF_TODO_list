from rest_framework import generics
from users.models import User
from .serializers import UserApiBaseSerializer, UserApiRoleSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserApiBaseSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserApiRoleSerializer
        return UserApiBaseSerializer
