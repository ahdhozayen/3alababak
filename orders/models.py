from django.db import models
from account.models import Supplier

# Create your models here.
class PurchaseOder(models.Model):
    code = models.CharField(max_length = 30)
    total_price =models.DeciamlField(max_length = 30)
    supplier =models.ForeignKey(Supplier,on_delete= models.CASCADE,)
    status =models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
