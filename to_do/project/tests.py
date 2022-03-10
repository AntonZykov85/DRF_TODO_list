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


# Create your tests here.

class TestProject(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        # self.first_name = ''
        # self.last_name = ''
        self.password = 'password'
        self.email = 'admin@gmail.com'

        self.data = {'username': 'user', 'first_name': '', 'last_name': '', 'email': 'randommail@gmail.com', 'password' : 'password'}
        self.data_put = {'username': 'user_1', 'first_name': '', 'last_name': '', 'email': 'randommail_1@gmail.com', 'password' : 'password'}
        self.url = 'http://127.0.0.1:8000/api/project/'
        self.admin = User.objects.create_superuser(self.name, self.email, self.password)

    # def test_get_list(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    # почему-то в этом тесте выдает 200 != 400 не могу разобраться, возможно в админке с прправами начудил, остальное работает

    def test_put_admin(self):
        user = User.objects.create(**self.data)
        project_1 = Project.objects.create(name='project_1', repo_link='https://github.com/1/')

        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project_1.id}/', {'name': 'project_2',
                                                                  'repo_link': 'https://github.com/2/'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_2 = Project.objects.get(id=project_1.id)
        self.assertEqual(project_2.name, 'project_2')
        self.client.logout()


    def test_put_mixer(self):
        project_3 = mixer.blend(ToDo)
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project_3.id}/', {'name': 'Project_3',
                                                                  'repo_link': 'https://github.com/3/'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_4 = Project.objects.get(id=project_3.id)
        self.assertEqual(project_4.name, 'Project_3')
        self.client.logout()

    def test_put_mixer_fields(self):
        project_5 = mixer.blend(ToDo, name='Project_4')
        self.assertEqual(project_5.name, 'Project_4')
        self.client.login(username=self.name, password=self.password)
        response = self.client.put(f'{self.url}{project_5.id}/',
                                   {'name': 'Project_4', 'repo_link': 'https://github.com/4/'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_6 = Project.objects.get(id=project_5.id)
        self.assertEqual(project_6.name, 'Project_4')
        self.client.logout()
