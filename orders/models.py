from django.db import models
from account.models import Supplier,Customer
from inventory.models import Item

# Create your models here.
class PurchaseOder(models.Model):
    code = models.CharField(max_length = 30)
    total_price =models.DecimalField(max_digits=10000,decimal_places = 3)
    supplier =models.ForeignKey(Supplier,on_delete= models.CASCADE,)
    status =models.CharField(max_length = 30)
    created_at = models.DateField(auto_now_add=True,null =True)
    updated_at = models.DateField(null =True)
    #date = models.DateField()
    created_by = models.IntegerField(default = None)
    updated_by = models.IntegerField(default = None)

class SalesOrder(models.Model):
    code = models.CharField(max_length = 30)
    total_price = models.DecimalField(max_digits=10000,decimal_places = 3)
    customer =models.ForeignKey(Customer,on_delete= models.CASCADE,)
    status =models.CharField(max_length = 30)
    created_at = models.DateField(auto_now_add=True,null =True)
    updated_at = models.DateField(null =True)
    #date = models.DateField()
    created_by = models.IntegerField(default = None)
    updated_by = models.IntegerField(default = None)



class PurchaseTransaction(models.Model):
    item = models.ForeignKey(Item,on_delete= models.CASCADE,)
    quantity =models.IntegerField()
    total_price = models.DecimalField(max_digits=10000,decimal_places = 3)
    purchase_order = models.ForeignKey(PurchaseOder,on_delete= models.CASCADE,)
    created_at = models.DateField(auto_now_add=True,null =True)
    updated_at = models.DateField(null =True)
    created_by = models.IntegerField(default = None)
    updated_by = models.IntegerField(default = None)


class SalesTransaction(models.Model):
    item = models.ForeignKey(Item,on_delete= models.CASCADE,)
    quantity =models.IntegerField()
    total_price = models.DecimalField(max_digits=10000,decimal_places = 3)
    purchase_order = models.ForeignKey(SalesOrder,on_delete= models.CASCADE,)
    created_at = models.DateField(auto_now_add=True,null =True)
    updated_at = models.DateField(null =True)
    created_by = models.IntegerField(default = None)
    updated_by = models.IntegerField(default = None)
