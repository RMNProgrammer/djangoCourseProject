from django.shortcuts import render
from django.http import HttpResponse
from Travel.forms import NameForm

def home(request):
    return render(request,"website/index.html")

def contact(request):
    return render(request,"website/contact.html")

def about(request):
    return render(request,"website/about.html")

def test_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name,email,subject,message)
            return HttpResponse('Your message has been successfully sent to support.')
        else:
            return HttpResponse('An error occurred, try again.')
    form = NameForm()
    return render(request,"test-form.html",{'form':form})