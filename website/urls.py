from django.contrib import admin
from django.urls import path, include
from website.views import (
    home,
    register_request,
    login_request,
    logout_request,
    about_request,
)
from website.urls_api import router

urlpatterns = [
    path('api', include(router.urls)),
    path("", home, name="home"),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
    path("about", about_request, name= "about"),
    ]
