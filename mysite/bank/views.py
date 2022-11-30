import re

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.db.models import F
from django.contrib import messages

from .forms import *
from .models import *

menu = [{'title': 'Main Page', 'url_name': 'home'},
        {'title': 'Registration', 'url_name': 'registration'},

        ]


def index(request):
    info = Users.objects.all()
    return render(request, 'bank/index.html', {'menu': menu, 'title': 'Main Page', 'info': info})


# class UserPage(ListView):
#     model = Users
#     form_class = AddUserForm
#     template_name = 'bank/user_page.html'
#     extra_context = {'menu': menu, 'title': 'Страница пользователя'}


# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'bank/sing_in.html'
#     extra_context = {'menu': menu, 'title': 'Авторизация'}


def user_page(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddUserForm()
    return render(request, 'bank/user_page.html', {'form': form, 'menu': menu, 'title': 'registration'})


# def sing_in(request):
#     return render(request, 'bank/sing_in.html')


def transfer(request):
    return render(request, 'bank/transfer.html')


def bringing_in(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        amount_of_funds = request.POST['amount_of_funds']
        info = Users.objects.filter(phone_number=phone_number, password=password)
        print(info)
        a = int(amount_of_funds)
        Users.objects.filter(phone_number=phone_number).update(amount_of_funds=F('amount_of_funds') + a)

        if info:
            return redirect('user')
        else:
            messages.warning(request, "Пользователя с такими данными не сущестует")
            return redirect('bringing_in')

    else:
        form = BringingInForm()
    return render(request, 'bank/bringing_in.html',
                  {'form': form, 'menu': menu, 'title': 'bringing_in'})


def about_card(request):

    return render(request, 'bank/about_card.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('ERRORRRRR')


class RegisterUser(CreateView):
    form_class = RegistrationUserForm
    template_name = 'bank/registration.html'
    success_url = reverse_lazy('user')
    extra_context = {'menu': menu, 'title': 'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'bank/sing_in.html'
    extra_context = {'menu': menu, 'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('user')


def logout_user(request):
    logout(request)
    return redirect('sing_in')
