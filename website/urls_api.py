from django.urls import include, path
from rest_framework import routers
from website import views_api as views 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)