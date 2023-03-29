from blog.feeds import LastestEntriesFeed
from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('',blog,name='blog'),
    path('<int:PostID>/',posts,name='posts'), 
    path('category/<str:cat_name>/',blog,name='category'),
    path('tag/<str:tag_name>',blog,name='tag'),
    path('author/<str:author_username>/',blog,name='author'),
    path('search/',search,name='search'),
    path('rss/',LastestEntriesFeed()),
    path('test/',test,name='test')   
] 