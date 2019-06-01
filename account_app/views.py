from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from account_app.models import MyUser, Buyer
from django.contrib import auth
from django.db.models import Q
import re


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
    if request.method == "POST":
        username = request.method.GET('username')
        password = request.method.GET('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, "login.html", {'errorMsg': '该用户不存在或密码错误'})
    return render(request, 'login.html')


def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        cardNum = request.POST.get('cardNum')
        nickName = request.POST.get('nickName')
        email_valid = r'^[0-9a-zA-Z\_\-]+(\.[0-9a-zA-Z\_\-]+)*@[0-9a-zA-Z]+(\.[0-9a-zA-Z]+){1,}$'

        if email:
            if not re.match(email_valid, email):
                return render(request, "register.html", {'errorMsg': '无效的邮箱地址'})
        if len(password) < 6:
            return render(request, "register.html", {'errorMsg': '密码不能少于6位'})
        if password != repassword:
            return render(request, "register.html", {'errorMsg': '两次输入密码不一致'})
        info = MyUser.objects.filter(username=username).first()
        if info is not None:
            return render(request, "register.html", {'errMsg': '该用户名已存在'})

        MyUser.objects.create_user(email=email, username=username, password=password, sex=gender, phone=phone)
        Buyer.objects.create(cardNum=cardNum, nickName=nickName)
        return HttpResponseRedirect('/login/')
    return render(request, 'register.html')
