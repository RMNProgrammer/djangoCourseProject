from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")

def contant(request):
    return HttpResponse("contant")

def about(request):
    return HttpResponse("about")