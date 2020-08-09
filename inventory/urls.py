from django.urls import path
from inventory import views

app_name = 'inventory'
urlpatterns = [
               path('category/list/', views.list_categorires_view, name='list-categories'),
               path('category/create/', views.create_category_view, name='create-category'),
               path('brands/list/', views.list_brands_view, name='list-brands'),
               path('attribute/list/', views.list_attributes_view, name='list-attributes'),
               path('product/list/', views.list_products_view, name='list-products'),
]
