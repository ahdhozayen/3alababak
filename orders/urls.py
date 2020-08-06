from django.urls import path
from orders import views

app_name = 'orders'
urlpatterns = [
    path('purchase/', views.create_purchaseOrder_view, name='create-po'),
    path('list/purchase-orders/', views.list_purchaseOrder_view, name='list-po'),
    path('update/purchase-order/<id>', views.update_purchaseOrder_view, name='update-po'),

]
