import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from project.models import Project, ToDo
from users.models import User
from .mutations_todo import ToDoType, ToDoUpdateMutation, ToDoCreateMutation, ToDoDeleteMutation
from .mutations_projects import ProjectType, ProjectUpdateMutation, ProjectCreateMutation, ProjectDeleteMutation

#EASY

# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value='Hola!')
#
#
# schema = graphene.Schema(query=Query)

# NORMAL

# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class ToDoType(DjangoObjectType):
#     class Meta:
#         model = ToDo
#         fields = '__all__'
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class Query(graphene.ObjectType):
#     users = graphene.List(UserType)
#     to_dos = graphene.List(ToDoType)
#     projects = graphene.List(ProjectType)
#
#
#     def resolve_users(root, info):
#         return User.objects.all()
#
#     def resolve_to_dos(root, info):
#         return ToDo.objects.all()
#
#     def resolve_projects(root, info):
#         return Project.objects.all()
#
#
#
# schema = graphene.Schema(query=Query)

#HARD

# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class ToDoType(DjangoObjectType):
#     class Meta:
#         model = ToDo
#         fields = '__all__'
#
#
# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# # фильтрация by id
#
# class Query(ObjectType):
#   user_id = graphene.Field(UserType, id=graphene.Int())
#
#   def resolve_user_id(root, info, id=None):
#       try:
#         return User.objects.get(id=id)
#       except User.DoesNotExist:
#         return None


# фильтрация по связанному полю


#     todos_by_creator = graphene.List(ToDoType, username=graphene.String(required=False))
#     def resolve_todos_by_creator(root, info, username=None):
#         to_dos = ToDo.objects.all()
#         if username:
#             to_dos = to_dos.filter(creator__username=username)
#         return to_dos



#     todos_by_project = graphene.List(ToDoType, name=graphene.String(required=False))
#
#     def resolve_todos_by_project(root, info, name=None):
#         to_dos = ToDo.objects.all()
#         if name:
#             to_dos = to_dos.filter(initial_project__name=name)
#         return to_dos
#
# schema = graphene.Schema(query=Query)

#HARDCORE


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(ObjectType):
    user_id = graphene.Field(UserType, id=graphene.Int())
    to_dos = graphene.Field(ToDoType, id=graphene.Int())
    projects = graphene.Field(ProjectType, id=graphene.Int())


class UserUpdateMutation(graphene.Mutation):

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, id):
        user = User.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return UserUpdateMutation(user=user)


class UserCreateMutation(graphene.Mutation):

    class Arguments:
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, email):
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.save()
        return UserCreateMutation(user=user)


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id):
        User.objects.get(id=id).delete()

        return UserDeleteMutation(user=None)




class Mutations(ObjectType):

    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()
    update_todos = ToDoUpdateMutation.Field()
    create_todos = ToDoCreateMutation.Field()
    delete_todos = ToDoDeleteMutation.Field()
    update_projects = ProjectUpdateMutation.Field()
    create_projects = ProjectCreateMutation.Field()
    delete_projects = ProjectDeleteMutation.Field()





schema = graphene.Schema(query=Query, mutation=Mutations)






