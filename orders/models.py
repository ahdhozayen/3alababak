from django.db import models
from djmoney.models.fields import MoneyField
from account.models import Supplier, Customer
from inventory.models import Item
from django.conf import settings


# Create your models here.
class PurchaseOder(models.Model):
    code = models.CharField(max_length=30)
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EGP')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, )
    status = models.CharField(max_length=8,
                              choices=[('recieved', 'Received'), ('retuned', 'Returned'), ('shipping', 'Shipping')])
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True, auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                   related_name="order_created_by")
    last_updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    # date = models.DateField()


    def __str__(self):
        return self.code


class SalesOrder(models.Model):
    code = models.CharField(max_length=30)
    total_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EGP')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, )
    status = models.CharField(max_length=8,
                              choices=[('recieved', 'Received'), ('retuned', 'Returned'), ('shipping', 'Shipping')])
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    # date = models.DateField()
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.code


class PurchaseTransaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10000, decimal_places=3)
    purchase_order = models.ForeignKey(PurchaseOder, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.purchase_order.code + " Transaction"


class SalesTransaction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10000, decimal_places=3)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.sales_order.code + " Transaction"
