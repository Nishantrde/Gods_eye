from django.urls import path
from .views import index, index_test, re_gen

urlpatterns = [
    path("", index),
    path("2",index_test),
    path("1111", re_gen),
    
]


