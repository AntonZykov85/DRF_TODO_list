from django.urls import path

from user_api.views import UserListAPIView

app_name = 'user_api'

urlpatterns = [
    path('', UserListAPIView.as_view())
]