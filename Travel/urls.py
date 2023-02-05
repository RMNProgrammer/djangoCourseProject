from django.urls import path
from .views import home,about,contant

urlpatterns = [
    path('',home),
    path('about/',about),
    path('contant/',contant)
]