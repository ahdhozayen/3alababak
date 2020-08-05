from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('/customer/', views.create_customer_address_account, name='customer'),
    path('supplier/', views.create_supplier_account, name='create-supplier'),
    path('list/supplier/', views.list_suppliers_view, name='list-suppliers'),
]
