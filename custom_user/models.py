from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    emp_type_list = [("A", _("Admin")),
                       ("E", _("Employee")) ]
    ############################################################################################
    employee_type = models.CharField(max_length=3, choices=emp_type_list, verbose_name=_('Employee Type'))
