from django.urls import path, include
from rest_framework import routers

from url import views

router = routers.DefaultRouter()
router.register(r"", views.UrlViewSet, basename="url")

url_urlpatterns = [
    path("", include(router.urls)),
]
