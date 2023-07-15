from django.urls import path
from .views import logout_view, registration_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", obtain_auth_token, name = "login"),
    path("register/", registration_view, name = "register"),
    path("logout/", logout_view, name = "logout")    
]