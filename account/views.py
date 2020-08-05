from django.shortcuts import render
from account.forms import CustomerCreationForm, SupplierCreationForm, AddressCreationForm, customer_address_formset, \
    supplier_address_formset, CompanyCreationForm
from django.forms import inlineformset_factory
from account.models import Customer, Supplier, Address


def list_suppliers_view(request):
    supliers_list = Supplier.objects.all()
    supContext = {
        'supliers_list': supliers_list,
    }
    return render(request, 'list-suppliers.html', supContext)


def create_customer_address_account(request):
    form, cust = create_customer(request)
    address = create_address(request, cust, customer_address_formset)
    req_form = {
        'supplier_form': form,
        'address_form': address
    }

    return render(request, 'create-supplier.html', context=req_form)


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


def create_supplier_address_account(request):
    form, supp = create_supplier(request)
    address = create_address(request, supp, supplier_address_formset)
    req_form = {
        'account_form': form,
        'address_form': address
    }

    return render(request, 'account.html', context=req_form)


def create_supplier(request):
    supplier_instance = None

    if request.method == 'POST':
        form = SupplierCreationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.created_by = request.user
            form.last_updated_by = request.user
            supplier_instance = form.save()
    else:
        form = SupplierCreationForm()
    return form, supplier_instance


def create_address(request, account_instance, address_formset):
    forms = address_formset()
    if request.method == 'POST':
        if account_instance is None:
            print("please enter valid account information")
        else:
            forms = address_formset(request.POST, instance=account_instance)
            for form in forms:
                if form.is_valid():
                    form.save(commit=False)
                    form.created_by = request.user
                    form.last_updated_by = request.user
                    form.save()
    return forms


def list_customers(request):
    customers = Customer.objects.all().values()
    supcontext = {'dict_customers': customers}
    return render(request, 'list_customers.html', context=supcontext)


def list_suppliers(request):
    suppliers = Supplier.objects.all().values()
    supcontext = {'dict_suppliers': suppliers}
    return render(request, 'list_suppliers.html', context=supcontext)


def create_company(request):
    form = CompanyCreationForm()
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            form.save()
    req_form = {'company_form': form}
    return render(request, 'company.html', context=req_form)
