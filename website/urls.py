from django.contrib import admin
from django.urls import path, include
from website.views import home
from website.urls_api import router

urlpatterns = [
    path('api/', include(router.urls)),
    path("", home, name="home"),
]
