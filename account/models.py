from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email =  models.EmailField()
    phone_number = models.CharField(max_length=30)
    landline = models.CharField(max_length=30,blank= True,null=True)
    status = models.BooleanField(default = False)
    company= models.ForeignKey('Company',on_delete=models.CASCADE,)
    created_at = models.DateField(auto_now_add=True,null =True)
    last_updated_at = models.DateField(null =True)
    created_by = models.IntegerField(null = True)
    last_updated_by = models.IntegerField(null = True)


    def __str__(self):
        return self.first_name+' '+self.last_name


class Supplier(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email =  models.EmailField()
    phone_number = models.CharField(max_length=30)
    landline = models.CharField(max_length=30,blank= True,null=True)
    status = models.BooleanField(default = False)
    company= models.ForeignKey('Company',on_delete=models.CASCADE,)
    created_at = models.DateField(auto_now_add=True,null =True)
    last_updated_at = models.DateField(null =True)
    created_by = models.IntegerField(null = True)
    last_updated_by = models.IntegerField(null = True)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Address(models.Model):
    customer =  models.ForeignKey('Customer',on_delete=models.CASCADE,blank=True,null=True)
    supplier = models.ForeignKey('Supplier',on_delete=models.CASCADE,blank=True,null=True)
    address= models.CharField(max_length=30,blank=True,null=True)
    country= models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    phone_number= models.CharField(max_length=30,blank= True,null=True)
    landline= models.CharField(max_length=30,blank= True,null=True)
    zip_code= models.CharField(max_length=30,null=True)
    created_at = models.DateField(auto_now_add=True,null =True)
    last_updated_at = models.DateField(null =True)
    created_by = models.IntegerField(null = True)
    last_updated_by = models.IntegerField(null = True)

    class Meta:
        verbose_name_plural = "Addresses"
    def __str__(self):
        return self.customer.first_name+'\'s address'



class Company(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True,null =True)
    last_updated_at = models.DateField(null =True)
    created_by = models.IntegerField(null = True,blank=True)
    last_updated_by = models.IntegerField(null = True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"
