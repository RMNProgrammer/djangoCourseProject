from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime

def blog(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now()).values()
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def posts(request,PostID):
    post = get_object_or_404(Post,id=PostID)
    post.counted_views += 1
    post.save()
    context = {'post':post}
    return render(request,'blog/posts.html',context)