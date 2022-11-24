from django.db import models


class Users(models.Model):
    FIO = models.CharField(max_length=255, blank=False)
    phone_number = models.IntegerField(blank=False)
    card_number = models.BigIntegerField(blank=False, unique=True)
    mail = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    amount_of_funds = models.IntegerField(default=0)
