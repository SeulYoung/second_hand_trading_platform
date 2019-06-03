from django.db import models
from account_app.models import MyUser, Buyer, Seller


class Commodity(models.Model):
    commodity_id = models.AutoField(primary_key=True, auto_created=100001)
    seller_id = models.ForeignKey('account_app.Seller', to_field='seller_id', on_delete=models.CASCADE)
    TYPE_CHOICE = (
        (0, u'手机'),
        (1, u'农用物资'),
        (2, u'生鲜水果'),
        (3, u'园艺植物'),
        (4, u'五金工具'),
        (5, u'电子零件'),
        (6, u'动漫/周边'),
        (7, u'宠物用品'),
        (8, u'网络设备'),
        (9, u'服饰/配饰'),
        (10, u'家装建材'),
        (11, u'家纺布艺'),
        (12, u'珠宝首饰'),
        (13, u'游戏'),
        (14, u'办公用品'),
        (15, u'图书'),
        (16, u'运动户外'),
        (17, u'票务娱乐'),
        (18, u'玩具'),
        (19, u'车辆'),
        (20, u'其他'),
    )
    type_id = models.CharField(max_length=15, choices=TYPE_CHOICE)
    name = models.CharField(max_length=30)
    pic = models.ImageField()
    price = models.IntegerField()
    number = models.IntegerField()
    desc = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class Favorites(models.Model):
    buyer_id = models.ForeignKey('account_app.Buyer', to_field='buyer_id', on_delete=models.CASCADE)
    commodity_id = models.ForeignKey('Commodity', to_field='commodity_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, auto_created=10000000)
    buyer_id = models.ForeignKey('account_app.Buyer', to_field='buyer_id', on_delete=models.CASCADE)
    commodity_id = models.ForeignKey('Commodity', to_field='commodity_id', on_delete=models.CASCADE)
    STATUS_CHOICE = (
        (0, u'待付款'),
        (1, u'待发货'),
        (2, u'待收货'),
        (3, u'待评价'),
        (4, u'已完成'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    buyer_id = models.ForeignKey('account_app.Buyer', to_field='buyer_id', on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', to_field='order_id', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


