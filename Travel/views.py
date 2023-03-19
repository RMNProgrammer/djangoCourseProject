from django.shortcuts import render
from django.http import HttpResponse
from Travel.forms import ContactForm

def home(request):
    return render(request,"website/index.html")

def contact(request):
    return render(request,"website/contact.html")

def about(request):
    return render(request,"website/about.html")

def test_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your message has been successfully sent to support.')
        else:
            return HttpResponse('An error occurred, try again.')
    form = ContactForm()
    return render(request,"test-form.html",{'form':form})