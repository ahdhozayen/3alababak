from django.shortcuts import render, redirect
from account.forms import (CustomerCreationForm, SupplierCreationForm, AddressCreationForm, customer_address_formset,
                           supplier_address_formset, CompanyCreationForm, )
from django.forms import inlineformset_factory
from account.models import Customer, Supplier, Address
from django.contrib import messages


def create_customer_address_account(request):
    if request.method == 'POST':
        customer_form = CustomerCreationForm(request.POST)
        address_inlineformset = customer_address_formset(request.POST)
        if customer_form.is_valid() and address_inlineformset.is_valid():
            customer_obj = customer_form.save(commit=False)
            customer_obj.created_by = request.user
            customer_obj.company = request.user.company
            customer_obj.save()
            address_inlineformset = customer_address_formset(request.POST, instance=customer_obj)
            for form in address_inlineformset:
                if form.is_valid():
                    address_obj = form.save(commit=False)
                    address_obj.created_by = request.user
                    address_obj.save()

            messages.success(request, 'Saved Successfully')
            return redirect('account:list-customers')
        else:
            print(customer_form.errors)
    else:
        customer_form = CustomerCreationForm()
        address_inlineformset = customer_address_formset()

    customer_information_context = {
        'account_form': customer_form,
        'address_inlineformset': address_inlineformset
    }
    return render(request, 'create-supplier.html', context=customer_information_context)


def create_supplier_address_account(request):
    if request.method == 'POST':
        supplier_form = SupplierCreationForm(request.POST)
        address_inlineformset = supplier_address_formset(request.POST)
        if supplier_form.is_valid() and address_inlineformset.is_valid():
            supplier_obj = supplier_form.save(commit=False)
            supplier_obj.created_by = request.user
            supplier_obj.company = request.user.company
            supplier_instance = supplier_obj.save()
            address_inlineformset = supplier_address_formset(request.POST, instance=supplier_instance)
            for form in address_inlineformset:
                if form.is_valid():
                    address_obj = form.save(commit=False)
                    address_obj.created_by = request.user
                    address_obj.save()

            messages.success(request, 'Saved Successfully')
            return redirect('account:list-suppliers')
        else:
            print(supplier_form.errors)
    else:
        supplier_form = SupplierCreationForm()
        address_inlineformset = supplier_address_formset()

    supplier_information_context = {
        'account_form': supplier_form,
        'address_inlineformset': address_inlineformset
    }

    return render(request, 'create-supplier.html', context=supplier_information_context)


def create_company(request):
    form = CompanyCreationForm()
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            form.save()
    req_form = {'company_form': form}
    return render(request, 'company.html', context=req_form)


def list_customers(request):
    customers = Customer.objects.all().values()
    supcontext = {'dict_customers': customers}
    return render(request, 'list_customers.html', context=supcontext)


def list_suppliers(request):
    suppliers = Supplier.objects.all().values()
    supcontext = {'dict_suppliers': suppliers}
    return render(request, 'list_suppliers.html', context=supcontext)


def list_suppliers_view(request):
    supliers_list = Supplier.objects.all()
    supContext = {
        'supliers_list': supliers_list,
    }
    return render(request, 'list-suppliers.html', supContext)


def list_customer_view(request):
    customers_list = Customer.objects.all()
    supContext = {
        'customers_list': customers_list,
    }
    return render(request, 'list-customers.html', supContext)
