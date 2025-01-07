from django.urls import path 
from .views import *

urlpatterns = [
    path('debug-static-files/', debug_static_files, name='debug_static_files'),
    path("", index),
]
