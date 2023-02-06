from django.shortcuts import render

def blog(request):
    return render(request,'blog/blog.html')

def posts(request):
    return render(request,'blog/posts.html')