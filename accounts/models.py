from django.db import models
from choices import *
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=250, null=True)


    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=250, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=250, null=True, choices=CATEGORY)
    description = models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    tags = models.ManyToManyField(Tag)


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=StatusChoice.choices, max_length=50)

