from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from project.models import Project, ToDo
from users.models import User

class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ('name', 'repo_link')


class ToDoModelSerializer(ModelSerializer):

    # initial_project = serializers.CharField(default=True)
    creation_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default=True )
    update_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", default=True)
    # creator = serializers.CharField(default=True)

    class Meta:
        model = ToDo
        # fields = '__all__'
        fields = ('id', 'initial_project', 'creator', 'note', 'creation_date', 'update_date')

    # def __str__(self):
    #     return self.creator,  self.initial_project
