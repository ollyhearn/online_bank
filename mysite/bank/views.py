from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = ['Main page', 'Sing_in', 'Registration']


def index(request):
    info = Users.objects.all()
    return render(request, 'bank/index.html', {'menu': menu, 'title': 'Main Page', 'info': info})


def user_page(request, user_name):
    return HttpResponse(f'user_page - {user_name}')


def registration(request):
    return HttpResponse(request, 'bank/registration.html')


def sing_in(request):
    return HttpResponse(request, 'bank/sing_in.html')


def transfer(request):
    return HttpResponse(request, 'bank/transfer.html')


def bringing_in(request):
    return HttpResponse(request, 'bank/bringing_in.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('ERRORRRRR')
