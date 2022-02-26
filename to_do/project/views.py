from django.shortcuts import render

from rest_framework import viewsets, mixins, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from project.filters import ProjectFilter, TODOFilter
from project.models import Project, ToDo
from project.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(viewsets.ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = TODOFilter

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)