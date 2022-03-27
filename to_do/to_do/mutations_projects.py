import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from project.models import Project



class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class Query(ObjectType):
    projects = graphene.Field(ProjectType)



class ProjectUpdateMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        repo_link = graphene.String(required=True)
        id = graphene.ID()

    projects = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, repo_link, id):
        projects = Project.objects.get(id=id)
        projects.name = name
        projects.repo_link = repo_link
        projects.save()
        return ProjectUpdateMutation(projects=projects)


class ProjectCreateMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=True)
        repo_link = graphene.String(required=True)
        users = graphene.ID(required=True)

    projects = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, repo_link, users):
        projects = Project(name=name, repo_link=repo_link, users=users)
        projects.save()
        return ProjectCreateMutation(projects=projects)


class ProjectDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    projects = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, id):
        Project.objects.get(id=id).delete()

        return ProjectDeleteMutation(projects=None)