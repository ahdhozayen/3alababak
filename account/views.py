from django.shortcuts import render
from account.forms import CustomerCreationForm, SupplierCreationForm, AddressCreationForm
from django.forms import inlineformset_factory
from account.models import Customer, Supplier, Address


def list_suppliers_view(request):
    supliers_list = Supplier.objects.all()
    supContext = {
                  'supliers_list':supliers_list,
    }
    return render(request, 'list-suppliers.html', supContext)


def create_customer_address_account(request):
    form, cust = create_customer(request)
    address = create_address(request, cust)
    req_form = {
                'account_form': form,
                'address_form': address
                }

    return render(request, 'account.html', context=req_form)


def create_customer(request):
    customer_instance = None
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.created_by = request.user
            form.last_updated_by = request.user
            customer_instance = form.save()
    else:
        form = CustomerCreationForm()
    return form, customer_instance


def create_supplier_account(request):
    if request.method == 'POST':
        form = SupplierCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.created_by = request.user
            form.last_updated_by = request.user
            form.save()
    else:
        form = SupplierCreationForm()
    req_form = {'form': form}
    return render(request, 'account.html', context=req_form)


def create_address(request, account_instance):
    AddressFormSet = inlineformset_factory(Customer, Address,
                                           form=AddressCreationForm, extra=1)

    forms = AddressFormSet()
    if request.method == 'POST':
        if account_instance is None:
            print("please enter valid account information")
        else:
            forms = AddressFormSet(request.POST,instance=account_instance)
            for form in forms:
                if form.is_valid():
                    form.save(commit=False)
                    form.created_by = request.user
                    form.last_updated_by = request.user
                    form.save()
    return forms
