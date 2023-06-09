"""url_shortener URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from client.urls import client_urlpatterns
from url.urls import url_urlpatterns
from front_view.urls import front_view_urlpatters

schema_view = get_schema_view(
    openapi.Info(
        title="URL Shortener",
        default_version='v1',
        contact=openapi.Contact(email="mh.bakhshipour@yahoo.com"),
    ),
    public=True,
)

auth_urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

api_urlpatters = [
    path("auth/", include(auth_urlpatterns)),
    path("client/", include(client_urlpatterns)),
    path("url/", include(url_urlpatterns)),
]

urlpatterns = [
    path("api/", include(api_urlpatters)),
    path("admin/", admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    path("", include(front_view_urlpatters)),
]
urlpatterns += staticfiles_urlpatterns()
