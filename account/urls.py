from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('customer/', views.create_customer_address_account, name='customer'),
    path('supplier/', views.create_supplier_address_account, name='create-supplier'),
    path('list/suppliers/', views.list_suppliers_view, name='list-suppliers'),
    path('list/customers/', views.list_customers, name='list_customers'),
    path('company/', views.create_company, name='company'),

]
