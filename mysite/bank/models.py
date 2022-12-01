from django.db import models


class Users(models.Model):
    FIO = models.CharField(max_length=255)
    phone_number = models.IntegerField(unique=True)
    card_number = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=255)
    amount_of_funds = models.IntegerField(default=0)

