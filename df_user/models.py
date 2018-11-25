from django.db import models


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=40)
    user_email = models.CharField(max_length=30)
    accepter_name = models.CharField(max_length=10, default='')
    accepter_address = models.CharField(max_length=100, default='')
    accepter_postcode = models.CharField(max_length=6, default='')
    accepter_phone_number = models.CharField(max_length=11, default='')
