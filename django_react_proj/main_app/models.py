# file django_react_proj\main_app\models.py

from django.db import models
from django.urls import reverse
import datetime

from django.contrib.auth.models import User
class Categories(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(blank=True, null=True, upload_to='stock-flow-category-image')
    # number = models.IntegerField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category')

class Product(models.Model):
    name = models.CharField(max_length=100)
    purchaseCost = models.DecimalField(decimal_places=3, max_digits=10)
    salePrice = models.DecimalField(decimal_places=3, max_digits=10)
    image = models.FileField(blank=True, null=True, upload_to='stock-flow-product-image')
    categoryId = models.ForeignKey(Categories , on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('productList')

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customerList')

class SaleOrder(models.Model):
    saleDate = models.DateField(default=datetime.date.today)
    saleNote = models.TextField()
    confirmed = models.BooleanField(default=False)
    customerId = models.ForeignKey(Customer , on_delete=models.PROTECT)

    def __str__(self):
        return f"Sale Order ({self.id})"

    def get_absolute_url(self):
        return reverse('saleList')

class SaleOrderLine(models.Model):
    quantity = models.IntegerField()
    saleId = models.ForeignKey(SaleOrder , on_delete=models.PROTECT)
    productId = models.ForeignKey(Product , on_delete=models.PROTECT)

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vendorList')

class PurchaseOrder(models.Model):
    purchaseDate = models.DateField()
    purchaseNote = models.TextField()
    confirmed = models.BooleanField(default=False)
    vendorId = models.ForeignKey(Vendor , on_delete=models.PROTECT)

    def __str__(self):
        return f"Purchase Order ({self.id})"

    def get_absolute_url(self):
        return reverse('purchaseList')

class PurchaseOrderLine(models.Model):
    quantity = models.IntegerField()
    purchaseId = models.ForeignKey(PurchaseOrder , on_delete=models.PROTECT)
    productId = models.ForeignKey(Product , on_delete=models.PROTECT)