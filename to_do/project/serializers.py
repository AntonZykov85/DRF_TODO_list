from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from project.models import Project, ToDo

class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'repo_link')


class ToDoModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'
        # fields = ('initial_project', 'creator', 'note')
