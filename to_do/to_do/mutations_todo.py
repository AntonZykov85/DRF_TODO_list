import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from users.models import User
from project.models import Project, ToDo




class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(ObjectType):
    to_dos = graphene.Field(ToDoType)



class ToDoUpdateMutation(graphene.Mutation):

    class Arguments:
        note = graphene.String(required=True)
        id = graphene.ID()

    to_do = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, note, id):
        to_do = ToDo.objects.get(id=id)
        to_do.note = note
        to_do.save()
        return ToDoUpdateMutation(to_do=to_do)


class ToDoCreateMutation(graphene.Mutation):

    class Arguments:
        initial_project = graphene.ID()
        note = graphene.String(required=True)
        creator = graphene.ID()

    to_do = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, initial_project, note, creator):
        to_do = ToDo(initial_project=initial_project, note=note, creator=creator)
        to_do.save()
        return ToDoCreateMutation(to_do=to_do)


class ToDoDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    to_do = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, id):
        ToDo.objects.get(id=id).delete()

        return ToDoDeleteMutation(to_do=None)