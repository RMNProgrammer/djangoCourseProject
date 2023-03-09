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
    if published_posts.first().id != currentPost.id:
        next_posts = published_posts.filter(published_date__gt=currentPost.published_date)
        next_post = next_posts[next_posts.count()-1]
    else:
        next_post = None
    if published_posts.last().id != currentPost.id:
        pre_post = published_posts.filter(published_date__lt=currentPost.published_date)[0]
    else:
        pre_post = None
    currentPost.counted_views += 1
    currentPost.save()
    context = {'post':currentPost,'next_post':next_post,'pre_post':pre_post}
    return render(request,'blog/posts.html',context)

def test(request):
    return render(request,"test.html")

def blog_category(request,cat_name):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)