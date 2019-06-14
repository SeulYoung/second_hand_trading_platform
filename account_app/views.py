from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from account_app.models import MyUser, Buyer, Seller
from commodity_app.models import Commodity, Order
from django.contrib import auth
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
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
    is_exist = False
    com_list = Commodity.objects.all()
    if com_list:
        is_exist = True
    if request.user.is_authenticated:
        is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
        is_seller = Seller.objects.filter(seller_id=request.user).first()
        if is_seller.isActive:
            return redirect('sellerhome')
        else:
            return render(request, 'index.html',
                          {'is_buyer': is_buyer, 'is_seller': is_seller, 'com_list': com_list, 'is_exist': is_exist})
    return render(request, 'index.html', {'com_list': com_list, 'is_exist': is_exist})


@csrf_protect
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('../')
            else:
                return render(request, "login.html", {'errorMsg': '该用户不存在或密码错误'})
    return render(request, 'login.html')


@csrf_protect
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

        user = MyUser.objects.create_user(email=email, username=username, password=password)
        MyUser.objects.filter(username=username).update(sex=gender, phone=phone)
        Buyer.objects.create(buyer_id=user, cardNum=cardNum, nickName=nickName, isActive=True)
        Seller.objects.create(seller_id=user, isActive=False)
        return HttpResponseRedirect('/login/')
    return render(request, 'register.html')


@login_required(login_url='')
def logout(request):
    auth.logout(request)
    return redirect('index')


def switch(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    if is_buyer.isActive == True:
        Buyer.objects.filter(buyer_id=request.user).update(isActive=False)
        Seller.objects.filter(seller_id=request.user).update(isActive=True)
        return redirect('sellerhome')
    else:
        Buyer.objects.filter(buyer_id=request.user).update(isActive=True)
        Seller.objects.filter(seller_id=request.user).update(isActive=False)
        return redirect('index')


def sellerhome(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    my_commodity = Commodity.objects.filter(seller_id=is_seller)
    my_order = []
    for com in my_commodity:
        order = Order.objects.filter(commodity_id=com)
        for ord in order:
            my_order.append(ord)
    return render(request, "sellerhome.html", {'is_buyer': is_buyer, 'is_seller': is_seller,
                                               'my_commodity': my_commodity, 'my_order': my_order})


@csrf_protect
def personalinf(request):
    if request.method == 'POST':
        return redirect('exchange')
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    return render(request, 'personalinf.html', {'is_buyer': is_buyer, 'is_seller': is_seller})


@csrf_protect
def exchange(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    if request.method == 'POST':
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        cardNum = request.POST.get('cardNum')
        nickName = request.POST.get('nickName')
        shopName = request.POST.get('shopname')
        desc = request.POST.get('desc')
        MyUser.objects.filter(user_id=request.user.user_id).update(phone=phone, sex=gender)
        Buyer.objects.filter(buyer_id=request.user).update(cardNum=cardNum, nickName=nickName)
        Seller.objects.filter(seller_id=request.user).update(shopName=shopName, desc=desc)
        return HttpResponseRedirect('/personalinf/')
    return render(request, "exchange.html", {'is_buyer': is_buyer, 'is_seller': is_seller})


def password_update(request):
    is_buyer = Buyer.objects.filter(buyer_id=request.user).first()
    is_seller = Seller.objects.filter(seller_id=request.user).first()
    if request.method == 'POST':
        password = request.POST.get('password')
        newpassword = request.POST.get('newpassword')
        repassword = request.POST.get('repassword')
        if len(password) < 6:
            return render(request, "password_update.html", {'errorMsg': '密码不能少于6位',
                                                            'is_buyer': is_buyer, 'is_seller': is_seller})
        if newpassword != repassword:
            return render(request, "password_update.html", {'errorMsg': '两次输入密码不一致',
                                                            'is_buyer': is_buyer, 'is_seller': is_seller})
        if request.user.check_password(password):
            request.user.set_password(newpassword)
            request.user.save()
            return redirect('/login')
        else:
            return render(request, "password_update.html", {'errorMsg': '原密码错误',
                                                            'is_buyer': is_buyer, 'is_seller': is_seller})
    return render(request, "password_update.html", {'is_buyer': is_buyer, 'is_seller': is_seller})
