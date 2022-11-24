from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = [{'title': 'Main Page', 'url_name': 'home'},
        {'title': 'Registration', 'url_name': 'registration'},
        {'title': 'Sing_in', 'url_name': 'sing_in'},
        ]


def index(request):
    info = Users.objects.all()
    return render(request, 'bank/index.html', {'menu': menu, 'title': 'Main Page', 'info': info})


def user_page(request, user_name):
    return HttpResponse(f'user_page - {user_name}')


def registration(request):
    info = Users.objects.all()
    return render(request, 'bank/registration.html', {'menu': menu, 'title': 'registration', 'info': info})


def sing_in(request):
    return render(request, 'bank/sing_in.html')


def transfer(request):
    return render(request, 'bank/transfer.html')


def bringing_in(request):
    return render(request, 'bank/bringing_in.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('ERRORRRRR')
