from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def Sign_up(request):
    return render(request,'accounts/sign_up.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'accounts/login.html')

#def logout(request):
#    return