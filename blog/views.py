from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime

def blog(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def posts(request,PostID):
    published_posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    currentPost = get_object_or_404(published_posts,id=PostID)
    currentPost.counted_views += 1
    currentPost.save()
    context = {'post':currentPost}
    return render(request,'blog/posts.html',context)