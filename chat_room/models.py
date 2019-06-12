from django.db import models
from account_app.models import MyUser, Buyer, Seller, CustomerService


class Communication(models.Model):
    websocket_id = models.CharField(max_length=1024)
    # from_user = models.ForeignKey('account_app.MyUser', related_name='from_user', to_field='user_id',
    #                              db_column='from_user', on_delete=models.CASCADE)
    # to_user = models.ForeignKey('account_app.MyUser', related_name='to_user', to_field='user_id',
    #                              db_column='to_user', on_delete=models.CASCADE)
    from_user = models.CharField(max_length=1024)
    to_user = models.CharField(max_length=1024)
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
