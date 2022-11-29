from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=200, default='default')
    password = models.CharField(max_length=200, default='default', null=False)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    userID = models.CharField(max_length=50)
    timecreated = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    productID = models.CharField(max_length=50)
    name = models.CharField(max_length=300)
    detail = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    amount = models.IntegerField()
    timecreated = models.DateTimeField(auto_now_add=True)
