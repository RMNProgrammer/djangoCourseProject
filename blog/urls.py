from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',blog,name='blog'),
    path('posts/',posts,name='posts'),
]