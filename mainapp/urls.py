from django.urls import path
from .views import index, index_test

urlpatterns = [
    path("", index),
    path("2",index_test),
]


