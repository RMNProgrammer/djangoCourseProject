from django.shortcuts import render
from blog.models import Post

def blog(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog.html',context)

def posts(request):
    return render(request,'blog/posts.html')

#def test(request):
#    posts = Post.objects.all()
#    context = {'posts':posts}
#    return render(request,'test.html',context)