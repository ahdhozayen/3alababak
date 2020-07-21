from django.db import models
from account.models import company

# Create your models here.
class location(models.Model):
    company = models.ForeignKey(company,on_delete =models.CASCADE,)
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

    def __str__(self):
        return self.name
