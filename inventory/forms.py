from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from inventory.models import (Category, Brand, Attribute, Uom, Item, Product,)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ('company', 'created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        
category_model_formset = modelformset_factory(Category, form=CategoryForm, extra=3, can_delete=False)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        exclude = ('company', 'created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


class UOMForm(forms.ModelForm):
    class Meta:
        model = Uom
        fields = '__all__'
        exclude = ('company', 'created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(UOMForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('company', 'created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'

# customer_address_formset = inlineformset_factory(Customer, Address, form=AddressCreationForm, extra=3, can_delete=False)
