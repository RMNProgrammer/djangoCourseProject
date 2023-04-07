from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import registerForm

def Sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.email = form.cleaned_data.get('email')
                user.save()
                return redirect('/accounts/login/')
        return render(request,'registration/sign_up.html')
    else:
        return redirect('/')

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
        return render(request,'registration/login.html')
    else:
        return redirect('/')