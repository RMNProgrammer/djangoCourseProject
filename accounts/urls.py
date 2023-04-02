from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [    
    # registeration / sign-up
    path('sign-up/',Sign_up,name='sign-up'), 
    # login
    path('login/',Login,name='login'),
    # logout
    path('logout/',Logout,name='logout') 
]