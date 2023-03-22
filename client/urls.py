from django.urls import path, include
from rest_framework import routers

from client import views

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet, basename="user")

client_urlpatterns = [
    path("", include(router.urls)),
]
