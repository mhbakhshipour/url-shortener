from django.urls import path

from front_view.views import *

front_view_urlpatters = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('create-short-link/', create_short_link, name='create_short_link'),
    path('<str:short_url_id>/', short_url_view, name='short_url'),
]
