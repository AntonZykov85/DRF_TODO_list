from django.urls import path

from user_api.views import UserAPIView

app_name = 'user_api'

urlpatterns = [
    path('', UserAPIView.as_view())
]