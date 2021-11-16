from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def latestPapers(request):
    return render(request, 'latestPapers.html')

def registration(request):
    return render(request, 'registration.html')


