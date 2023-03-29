from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [    
    # registeration / sign-up
    path('sign-up/',sign_up,name='sign-up'),
    # login
    path('login/',login,name='login'),
    # logout
    #path('logout/',logout,name='logout') 
]