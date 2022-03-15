from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserApiSerializer, UserApiBaseSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserApiSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserApiBaseSerializer
        return UserApiSerializer