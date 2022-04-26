from django.shortcuts import render
from .models import Menu, About


# Create your views here.
def home(request):
    return render(request,'home.html')
    # return render(request, 'base.html')


def menu(request):
    menu = Menu.objects.all()
    print('HI')
    print(menu)
    print("Hello")
    return render(request, 'menu.html', context={'menu': menu})


def delivery(request):
    return render(request, 'services.html')


def about(request):
    about = About.objects.all()
    # print('Hlw')
    # print(about)
    # print("Hello")
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def contact(request):
    return render(request, 'contact.html')
