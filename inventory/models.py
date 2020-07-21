from django.db import models
from account.models import Company
from location.models import Location

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150,blank= True,null=True)
    company = models.ForeignKey(Company,on_delete= models.CASCADE,)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150,blank= True,null=True)
    company = models.ForeignKey(Company,on_delete= models.CASCADE,)
    parent_category = models.ForeignKey('Category',on_delete= models.CASCADE,blank=True,null= True)
    class meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Uom(models.Model):
    name =models.CharField(max_length = 30)
    type =models.CharField(max_length = 30)
    description=models.CharField(max_length = 150,blank= True,null=True)
    company = models.ForeignKey(Company,on_delete= models.CASCADE,)

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company,on_delete= models.CASCADE,)
    brand= models.ForeignKey(Brand,on_delete= models.CASCADE,)
    category=models.ForeignKey(Category,on_delete= models.CASCADE,)
    name = models.CharField(max_length = 30)
    description =models.CharField(max_length = 30,blank= True,null=True)
    uom=models.ForeignKey(Uom,on_delete= models.CASCADE,)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    name =models.CharField(max_length = 30)
    display_name =models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):
    product =models.ForeignKey(Product,on_delete= models.CASCADE,)
    attribute=models.ForeignKey(Attribute,on_delete= models.CASCADE,)

    def __str__(self):
        return self.product.name+' '+self.attribute.name

class Item(models.Model):
    name =models.CharField(max_length = 30)
    image =models.FileField(upload_to='uploads/')
    description =models.CharField(max_length = 30,blank= True,null=True)
    quantity =models.IntegerField()
    avg_cost =models.DecimalField(max_digits=10000,decimal_places = 3)
    selling_price =models.DecimalField(max_digits=10000,decimal_places = 3)
    sku =models.CharField(max_length = 30)
    barcode =models.CharField(max_length = 30)
    tax=models.BooleanField(max_length = 30)
    product =models.ForeignKey(Product,on_delete= models.CASCADE,)
    location =models.ForeignKey(Location,on_delete= models.CASCADE,)
    uom=models.ForeignKey(Uom,on_delete= models.CASCADE,)

    def __str__(self):
        return self.name

class ItemAttributeValue(models.Model):
    item =models.ForeignKey(Item,on_delete= models.CASCADE,)
    attribute=models.ForeignKey(Attribute,on_delete= models.CASCADE,)
    value = models.CharField(max_length = 30)

    def __str__(self):
        return self.item.name+' '+self.attribute.name
