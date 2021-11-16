from django.shortcuts import render,redirect

from .models import Contact
from django.contrib import messages

# Create your views here.
def contactus(request):
    if request.method == "POST":
        contact = Contact()
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        message1 = request.POST.get('message')

        contact.name = name1
        contact.email = email1
        contact.message = message1
        contact.save()

        messages.info(request,'Thanks For Contact Us')
        return redirect('/')
    return render(request, 'contact.html')