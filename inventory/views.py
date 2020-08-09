from django.shortcuts import render, redirect
from django.contrib import messages
from inventory.models import (Category, Brand, Product, Attribute, Item, Uom)
from inventory.forms import (CategoryForm, category_model_formset, BrandForm, ProductForm, UOMForm)


def create_category_view(request):
    category_formset = category_model_formset(queryset=None)
    if request.method == 'POST':
        category_formset = category_model_formset(request.POST)
        if category_formset.is_valid():
            category_obj = category_formset.save(commit=False)
            for form in category_obj:
                form.company = request.user.company
                form.created_by = request.user
                form.save()
            return redirect('inventory:list-categories')
    categoryContext = {
                       'category_formset': category_formset
                       }
    return render(request, 'create-category.html', context=categoryContext)


def list_categorires_view(request):
    categories_list = Category.objects.all()
    categoryContext = {
                  'categories_list': categories_list
                  }
    return render(request, 'list-categories.html', context=categoryContext)



def list_brands_view(request):
    brands_list = Brand.objects.all()
    brandsContext = {
                  'brands_list': brands_list
                  }
    return render(request, 'list-brands.html', context=brandsContext)


def list_attributes_view(request):
    attributes_list = Attribute.objects.all()
    attributesContext = {
                  'attributes_list': attributes_list
                  }
    return render(request, 'list-attributes.html', context=attributesContext)


def list_products_view(request):
    products_list = Product.objects.all()
    productsContext = {
                  'products_list': products_list
                  }
    return render(request, 'list-products.html', context=productsContext)
