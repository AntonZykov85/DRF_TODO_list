from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework import viewsets, mixins, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project.filters import ProjectFilter, TODOFilter
from project.models import Project, ToDo
from project.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    permission_classes = [IsAuthenticated]

class ToDoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer

    # @login_required
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         instance.is_active = False
    #         instance.save()
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    # @login_required
    # def ToDo_remove(request, ToDo_id):
    #     ToDo.objects.get(id=ToDo_id).delete()
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
