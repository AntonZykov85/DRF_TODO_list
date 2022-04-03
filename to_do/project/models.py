from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=150, blank=False)
    repo_link = models.URLField()
    users = models.ManyToManyField(User)
    #
    # def __str__(self):
    #     return f'{self.name}'


class ToDo(models.Model):
    initial_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.TextField(blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    field_is_active = models.BooleanField(default=True)

