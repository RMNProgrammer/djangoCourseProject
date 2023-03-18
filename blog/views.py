from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Post
import datetime

def blog(request,**kwargs):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        pass
    except EmptyPage:
        pass
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

def search(request):    
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now())
    if request.method == 'GET':
        if keySearch := request.GET.get('s'):
            posts = posts.filter(content__contains=keySearch)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def test(request):
    return render(request,"test-template-tags.html")