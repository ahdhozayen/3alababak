from django.db import models
from djmoney.models.fields import MoneyField
from account.models import Company
from location.models import Location


class Brand(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    parent_category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    class meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Uom(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=150, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=30)
    display_name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.product.name + ' ' + self.attribute.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='uploads/', blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.IntegerField()
    avg_cost = MoneyField(max_digits=14, decimal_places=2, default_currency='EGP')
    selling_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EGP')
    sku = models.CharField(max_length=30)
    barcode = models.CharField(max_length=30)
    tax = models.BooleanField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    location = models.ForeignKey(Location, on_delete=models.CASCADE, )
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE, )
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class ItemAttributeValue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, )
    value = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True, null=True)
    last_updated_at = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    last_updated_by = models.IntegerField(null=True)

    def __str__(self):
        return self.item.name + ' ' + self.attribute.name


class StokeTake(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name


class StokeEntry(models.Model):
    stoke_take = models.ForeignKey(StokeTake, on_delete=models.CASCADE, )
    item = models.ForeignKey(Item, on_delete=models.CASCADE, )
    quantity = models.IntegerField(null=True, blank=False)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name
