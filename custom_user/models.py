from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from account.models import Company


class User(AbstractUser):
    type = models.CharField(max_length=30, null=True, default='admin')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
