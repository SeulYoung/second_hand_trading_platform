from django.db import models
from account_app.models import MyUser, Buyer, Seller


class Commodity(models.Model):
    commodity_id = models.AutoField(primary_key=True, auto_created=100001)
    seller_id = models.ForeignKey('account_app.Seller', to_field='seller_id', on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=15, default=None)
    name = models.CharField(max_length=30, default=None)
    pic = models.ImageField(upload_to='images/%Y/%m/%d/')
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
    status = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    buyer_id = models.ForeignKey('account_app.Buyer', to_field='buyer_id', on_delete=models.CASCADE)
    order_id = models.ForeignKey('Order', to_field='order_id', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)


