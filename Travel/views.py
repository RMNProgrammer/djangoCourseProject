from django.shortcuts import render
from Travel.models import Contact

def home(request):
    return render(request,"website/index.html")

def contact(request):
    return render(request,"website/contact.html")

def about(request):
    return render(request,"website/about.html")

def test_form(request):
    if request.method == 'POST':
        M = Contact()
        M.name = request.POST.get('name')
        M.email = request.POST.get('email')
        M.subject = request.POST.get('subject')
        M.message = request.POST.get('message')
        M.save()
    return render(request,"test-form.html")