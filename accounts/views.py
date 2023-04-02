from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def Sign_up(request):
    return render(request,'accounts/sign_up.html')

def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
        return render(request,'accounts/login.html',{'form':AuthenticationForm})
    else:
        return redirect('/')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')