from django.urls import path
from account import views

urlpatterns = [
    path('/customer/', views.create_customer_address_account, name='customer'),
    path('/supplier/', views.create_supplier_account, name='supplier'),
]
