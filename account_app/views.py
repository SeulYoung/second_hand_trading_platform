from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from account_app.models import MyUser
from django.contrib import auth
from django.db.models import Q


class MyBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MyUser.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'register.html')
