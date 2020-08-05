from django import forms
from account.models import Customer, Supplier, Address
from django.forms import inlineformset_factory


class CustomerCreationForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')


class SupplierCreationForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(SupplierCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


class AddressCreationForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('customer', 'supplier', 'created_at', 'last_updated_at', 'created_by', 'last_updated_by')
