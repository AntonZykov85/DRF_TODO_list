from rest_framework.serializers import ModelSerializer

from users.models import User


class UserApiSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserApiBaseSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('is_superuser', 'is_staff')