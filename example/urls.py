# example/urls.py
from django.urls import path

from example.views import index, counter


urlpatterns = [
    path('', index),
    path('counter/', counter),
]