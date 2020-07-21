from django.db import models
from account.models import company
from location.models import location

# Create your models here.
class brand(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150,blank= True,null=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150,blank= True,null=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,)
    parent_category = models.ForeignKey('category',on_delete= models.CASCADE,blank=True,null= True)
    class meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class UOM(models.Model):
    name =models.CharField(max_length = 30)
    type =models.CharField(max_length = 30)
    description=models.CharField(max_length = 150,blank= True,null=True)
    company = models.ForeignKey(company,on_delete= models.CASCADE,)

    def __str__(self):
        return self.name

class product(models.Model):
    company = models.ForeignKey(company,on_delete= models.CASCADE,)
    brand= models.ForeignKey(brand,on_delete= models.CASCADE,)
    category=models.ForeignKey(category,on_delete= models.CASCADE,)
    name = models.CharField(max_length = 30)
    description =models.CharField(max_length = 30,blank= True,null=True)
    UOM=models.ForeignKey(UOM,on_delete= models.CASCADE,)
    def __str__(self):
        return self.name

class attribute(models.Model):
    name =models.CharField(max_length = 30)
    display_name =models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class product_attribute(models.Model):
    product =models.ForeignKey(product,on_delete= models.CASCADE,)
    attribute=models.ForeignKey(attribute,on_delete= models.CASCADE,)
    def __str__(self):
        return self.product.name+' '+self.attribute.name

class item(models.Model):
    name =models.CharField(max_length = 30)
    image =models.FileField(upload_to='uploads/')
    description =models.CharField(max_length = 30,blank= True,null=True)
    quantity =models.IntegerField()
    avg_cost =models.DecimalField(max_digits=10000,decimal_places = 3)
    selling_price =models.DecimalField(max_digits=10000,decimal_places = 3)
    SKU =models.CharField(max_length = 30)
    barcode =models.CharField(max_length = 30)
    tax=models.BooleanField(max_length = 30)
    product =models.ForeignKey(product,on_delete= models.CASCADE,)
    location =models.ForeignKey(location,on_delete= models.CASCADE,)
    UOM=models.ForeignKey(UOM,on_delete= models.CASCADE,)
    def __str__(self):
        return self.name

class item_attribute_value(models.Model):
        item =models.ForeignKey(item,on_delete= models.CASCADE,)
        attribute=models.ForeignKey(attribute,on_delete= models.CASCADE,)
        value = models.CharField(max_length = 30)

        def __str__(self):
            return self.item.name+' '+self.attribute.name
