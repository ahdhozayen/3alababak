from django.urls import path
from orders import views

app_name = 'orders'
urlpatterns = [
    path('purchase/', views.create_purchaseOrder_view, name='create-po'),


]
