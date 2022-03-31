from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


# class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin, viewsets.GenericViewSet):
#
#     # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer



from django.shortcuts import render

class UserModelViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserModelSerializer
   # permission_classes = [IsAuthenticated]


