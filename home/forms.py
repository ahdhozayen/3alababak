from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from custom_user.models import User
from django.utils.translation import ugettext_lazy as _



class CustomUserCreationForm(UserCreationForm):
    company_name = forms.CharField(max_length=60, required=True, help_text='This Field is Required.',label=_('Company Name'))
    user_type = forms.CharField(max_length=40, required=True,label=_('User Type'))

    class Meta(UserCreationForm):
        model = User
        fields = ('company_name', 'user_type', 'username', 'email')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control parsley-validated'

class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'type', 'email')

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control parsley-validated'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'type', 'email')
