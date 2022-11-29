from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=200, default='default')
    password = models.CharField(max_length=200, default='default', null=False)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    timecreated = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=300)
    detail = models.CharField(max_length=500)
    type = models.CharField(max_length=100)
    amount = models.IntegerField()
    timecreated = models.DateTimeField(auto_now_add=True)


class RequestForm(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=100)
    productID = models.IntegerField(max_length=100)
    status = models.BooleanField(default=False)
    username = models.CharField(max_length=200)
    timecreated = models.DateTimeField(auto_now_add=True)
