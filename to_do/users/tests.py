from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer

import users
from users.views import UserModelViewSet
from users.models import User
from project.views import ProjectModelViewSet, ToDoModelViewSet
from project.models import Project,ToDo
from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer


# Create your tests here.
class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.username = 'admin'
        # self.first_name = ''
        # self.last_name = ''
        self.password = 'password'
        self.email = 'admin@gmail.com'

        self.data = {'username': 'user', 'first_name': '', 'last_name': '', 'email': 'randommail@gmail.com', 'password' : 'password'}
        self.data_put = {'username': 'user_1', 'first_name': '', 'last_name': '', 'email': 'randommail_1@gmail.com', 'password' : 'password'}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(self.username, self.email, self.password)

    #APIRequestFactory force_authenticate

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url,self.data,format='json')
        view = UserModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request,self.admin)
        view = UserModelViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code,  status.HTTP_201_CREATED)


    def test_put_guest(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.put(f'{self.url}{user.id}/',self.data_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_admin(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        client.login(username=self.username, password=self.password)
        response = client.put(f'{self.url}{user.id}/', self.data_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_ = User.objects.get(id=user.id)
        self.assertEqual(user_.username, self.data_put.get('username'))
        self.assertEqual(user_.first_name, self.data_put.get('first_name'))
        self.assertEqual(user_.last_name, self.data_put.get('last_name'))
        self.assertEqual(user_.email, self.data_put.get('email'))

        client.logout()

    def tearDown(self) -> None:
        pass