from django import forms
from orders.models import PurchaseOder
from django.forms import inlineformset_factory
from orders.models import PurchaseOder, PurchaseTransaction, SalesOrder, SalesTransaction
from djmoney.models.fields import MoneyField


class PurchaseOrderCreationForm(forms.ModelForm):
    class Meta:
        model = PurchaseOder
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')
        widgets = {
            'date': forms.TimeInput(attrs={'class': 'form-control tm', 'type': 'date', })
        }

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'total_price':
                self.fields[field].widget.attrs['class'] = 'form-control'

            elif self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


class PurchaseTransactionCreationForm(forms.ModelForm):
    class Meta:
        model = PurchaseOder
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(PurchaseTransactionCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'total_price':
                self.fields[field].widget.attrs['class'] = 'form-control'

            elif self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


class SaleOrderCreationForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')
        widgets = {
            'date': forms.TimeInput(attrs={'class': 'form-control tm', 'type': 'date', })
        }

    def __init__(self, *args, **kwargs):
        super(SaleOrderCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'total_price':
                self.fields[field].widget.attrs['class'] = 'form-control'

            elif self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


class SaleTransactionCreationForm(forms.ModelForm):
    class Meta:
        model = SalesTransaction
        exclude = ('created_at', 'last_updated_at', 'created_by', 'last_updated_by')

    def __init__(self, *args, **kwargs):
        super(SaleTransactionCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'total_price':
                self.fields[field].widget.attrs['class'] = 'form-control'

            elif self.fields[field].widget.input_type == 'checkbox':
                self.fields[field].widget.attrs['class'] = 'form-check-input'
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'


purchase_transaction_formset = inlineformset_factory(PurchaseOder, PurchaseTransaction,
                                                     form=PurchaseTransactionCreationForm, extra=3, can_delete=False)

sale_transaction_formset = inlineformset_factory(SalesOrder, SalesTransaction,
                                                     form=SaleTransactionCreationForm, extra=3, can_delete=False)
