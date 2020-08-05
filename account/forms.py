from django import forms
from account.models import Customer, Supplier, Address, Company
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


class CompanyCreationForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')


customer_address_formset = inlineformset_factory(Customer, Address,
                                                 form=AddressCreationForm, extra=3)
supplier_address_formset = inlineformset_factory(Supplier, Address,
                                                 form=AddressCreationForm, extra=3)
