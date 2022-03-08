from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer
from users.views import UserModelViewSet
from users.models import User
from project.views import ProjectModelViewSet, ToDoModelViewSet
from project.models import Project, ToDo
from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User


# Create your tests here.

class TestProjects(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'password'
        self.email = 'admin@gmail.com'

        self.data = {'username': 'user', 'first_name': '', 'last_name': '', 'email': 'randommail@gmail.com'}
        self.data_put = {'username': 'user_1', 'first_name': '', 'last_name': '', 'email': 'randommail_1@gmail.com'}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_put_admin(self):
        user = User.objects.create(**self.data)
        project = Project.objects.create(text='test', user=user)
        self.client.login(username=self.name,password=self.password)
        response = self.client.put(f'{self.url}{project.id}/', {'text': 'Project_text', 'user': project.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        project_ =Project.objects.get(id=project.id)
        self.assertEqual(project_.text, 'Project_text')
        self.client.logout()

    def test_put_mixer(self):

        project = mixer.blend(Biography)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project.id}/', {'text': 'Project_text', 'user': project.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_ = Project.objects.get(id=project.id)
        self.assertEqual(project_.text, 'Project_text')
        self.client.logout()

    def test_put_mixer_fields(self):
        project = mixer.blend(Project,text='Project_text')
        self.assertEqual(project.text, 'Project_text')
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project.id}/', {'text': 'Project_text', 'user': project.user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_ = Project.objects.get(id=project.id)
        self.assertEqual(project_.text, 'Project_text')
        self.client.logout()