from django.shortcuts import render


def home(request):
    return render(request, 'content/home.html')


def contact(request):
    return render(request, 'content/contact.html')