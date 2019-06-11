from django.db import models
from account_app.models import MyUser, Buyer, Seller


class Commodity(models.Model):
    commodity_id = models.AutoField(primary_key=True, auto_created=100001)
    seller_id = models.ForeignKey('account_app.Seller', to_field='seller_id', on_delete=models.CASCADE)
    type = models.CharField(max_length=15)
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


