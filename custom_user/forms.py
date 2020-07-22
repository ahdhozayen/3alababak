from django import forms
from custom_user.models import User
from account.models import Company
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    type = forms.CharField(max_length = 20)

    class meta:
        model = User
        fields= ('company','type','username','email')
