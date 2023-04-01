from django.shortcuts import render

def sign_up(request):
    return render(request,'accounts/sign_up.html')

def login(request):
    if request.user.is_authenticated:
        msg = f'user is authenticated as {request.user.username}'
    else:
        msg = 'user is not authenticated'
    return render(request,'accounts/login.html',{'message':msg})

#def logout(request):
#    return