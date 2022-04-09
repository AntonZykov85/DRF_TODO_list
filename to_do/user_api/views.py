from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.models import User
from .serializers import UserApiBaseSerializer, UserApiRoleSerializer


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserApiBaseSerializer
    # permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserApiRoleSerializer
        return UserApiBaseSerializer

