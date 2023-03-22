from django.urls import path, include, re_path
from rest_framework import routers

from url import views

router = routers.DefaultRouter()
router.register(r"", views.UrlViewSet, basename="url")

url_urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^short-url/(?P<path>.*)',
            views.ShortUrlViewSet.as_view(), name='short_url'),
]
