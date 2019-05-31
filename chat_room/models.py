from django.db import models
from account_app.models import MyUser, Buyer, Seller, CustomerService


class Communication(models.Model):
    chatter1 = models.OneToOneField('Buyer', to_field='buyer_id', on_delete=models.CASCADE)
    chatter2 = models.OneToOneField('Seller', to_field='seller_id', on_delete=models.CASCADE)
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)


class Complaint(models.Model):
    chatter1 = models.OneToOneField('Buyer', to_field='buyer_id', on_delete=models.CASCADE)
    chatter2 = models.OneToOneField('CustomerService', to_field='customerService_id', on_delete=models.CASCADE)
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
