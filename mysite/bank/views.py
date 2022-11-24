from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse('Hi')


def user_page(request, user_name):
    return HttpResponse(f'user_page - {user_name}')


def registration(request):
    return HttpResponse('registration')


def sing_in(request):
    return HttpResponse('sing_in')


def transfer(request):
    return HttpResponse('transfer')


def bringing_in(request):
    return HttpResponse('bringing_in')


def page_not_found(request, exception):
    return HttpResponseNotFound('ERRORRRRR')
