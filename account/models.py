from django.db import models

# Create your models here.
class customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email =  models.EmailField()
    phone_number = models.CharField(max_length=30)
    landline = models.CharField(max_length=30,blank= True)
    status = models.BooleanField(default = False)
    company= models.ForeignKey('company',on_delete=models.CASCADE,)


    def __str__(self):
        return self.first_name+' '+self.last_name


class supplier(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email =  models.EmailField()
    phone_number = models.CharField(max_length=30)
    landline = models.CharField(max_length=30,blank= True)
    status = models.BooleanField(default = False)
    company= models.ForeignKey('company',on_delete=models.CASCADE,)

    def __str__(self):
        return self.first_name+' '+self.last_name

class address(models.Model):
    customer =  models.ForeignKey('customer',on_delete=models.CASCADE,blank=True,null=True)
    supplier = models.ForeignKey('supplier',on_delete=models.CASCADE,blank=True,null=True)
    address= models.CharField(max_length=30)
    country= models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    phone_number= models.CharField(max_length=30,blank= True)
    landline= models.CharField(max_length=30,blank= True)
    zip_code= models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "addresses"
    def __str__(self):
        return self.customer.first_name+'\'s address'



class company(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "companies"
