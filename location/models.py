from django.db import models
from account.models import Company

# Create your models here.
class Location(models.Model):
    company = models.ForeignKey(Company,on_delete =models.CASCADE,)
    type = models.CharField(max_length  = 30)
    code =models.CharField(max_length  = 30)
    name =models.CharField(max_length  = 30)
    address =models.CharField(max_length  = 30)
    city =models.CharField(max_length  = 30)
    zip_code =models.CharField(max_length  = 30)
    phone_number =models.CharField(max_length  = 30)
    landline =models.CharField(max_length  = 30)
    number_of_products =models.IntegerField()
    manager_name=models.CharField(max_length  = 30)
    manager_mail =models.EmailField()
    manager_phone_number=models.CharField(max_length  = 30)
    created_at = models.DateField(auto_now_add=True,null =True)
    updated_at = models.DateField(null =True)
    created_by = models.IntegerField(default = None)
    updated_by = models.IntegerField(default = None)

    def __str__(self):
        return self.name
