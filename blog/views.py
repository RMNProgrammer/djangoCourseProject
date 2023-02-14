from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def posts(request,PostID):
    post = get_object_or_404(Post,id=PostID)
    if post.status != 0:
        post.counted_views += 1
        post.save()
    context = {'post':post}
    return render(request,'blog/posts.html',context)