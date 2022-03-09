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

class TestToDo(APITestCase):

    # def setUp(self) -> None:
    #     self.username = 'admin'
    #     # self.first_name = ''
    #     # self.last_name = ''
    #     self.password = 'password'
    #     self.email = 'admin@gmail.com'
    #
    #     self.data = {'username': 'user', 'first_name': '', 'last_name': '', 'email': 'randommail@gmail.com', 'password' : 'password'}
    #     self.data_put = {'username': 'user_1', 'first_name': '', 'last_name': '', 'email': 'randommail_1@gmail.com', 'password' : 'password'}
    #     self.url = '/api/users/'
    #     self.admin = User.objects.create_superuser(self.username, self.email, self.password)

    def test_get_list(self):
        response = self.client.get('http://127.0.0.1:8000/api/to_do/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_mixer(self):
        todo = mixer.blend(ToDo)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'http://127.0.0.1:8000/api/to_do/{todo.id}/', {'note': 'azazaz', 'creator': todo.creator.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK) \
        #AssertionError: 400 != 200 - в 39 стоке, буду признателн, если поможите разобраться в причине проблемы.

        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.note, 'azazaz')

