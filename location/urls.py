from django.urls import path
from location import views

app_name = 'location'

urlpatterns = [
    path('create/', views.create_location_view, name='create-location'),
    path('update/', views.update_location_view, name='update-location'),
    path('list/locations/', views.list_location_view, name='list-locations'),
    path('delete/', views.delete_location_view, name='delete-location'),
]
