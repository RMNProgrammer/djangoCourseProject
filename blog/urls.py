from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',blog,name='blog'),
    path('<int:PostID>/',posts,name='posts'),   
]