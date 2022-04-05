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


    class Meta:
        model = ToDo
        fields = '__all__'
        # fields = ('initial_project', 'creator', 'note')









    # def __str__(self):
    #     return self.creator
    # initial_project = serializers.CharField()
    # creation_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    # update_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    # creator = serializers.CharField()