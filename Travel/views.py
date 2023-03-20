from django.http import HttpResponse, HttpResponseRedirect
from Travel.forms import ContactForm, NewsletterForm
from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request,"website/index.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket sended successfully.')
        else:
            messages.add_message(request,messages.WARNING,'An error occurred, the ticket could not be sent.')
    form = ContactForm()
    return render(request,"website/contact.html",{'contact':form})

def about(request):
    return render(request,"website/about.html")

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

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