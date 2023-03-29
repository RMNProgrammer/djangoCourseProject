from django.shortcuts import render

def sign_up(request):
    return render(request,'accounts/sign_up.html')

def login(request):
    return render(request,'accounts/login.html')

#def logout(request):
#    return