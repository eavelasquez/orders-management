from django.shortcuts import render

from ServicesApp.models import Service

# Create your views here.


def home(request):
    return render(request, 'WebAppWithDjango/home.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'WebAppWithDjango/services.html', {'services': services})

def shop(request):
    return render(request, 'WebAppWithDjango/shop.html')


def blog(request):
    return render(request, 'WebAppWithDjango/blog.html')


def contact(request):
    return render(request, 'WebAppWithDjango/contact.html')
