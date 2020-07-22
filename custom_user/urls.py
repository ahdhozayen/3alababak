from django.contrib import admin
from django.urls import path
from custom_user import views

urlpatterns = [
    path('',views.register,name ='register'),
]
