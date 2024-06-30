from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView

app_name = UsersConfig.name


urlpatterns = [
    path('',  LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('password_reset', RegisterView.as_view(), name='password_reset'),
    ]
