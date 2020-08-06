from django.shortcuts import render, redirect
from django.contrib import messages
from location.models import Location
from location.forms import LocationCreationForm


def list_location_view(request):
    locations_list = Location.objects.all()
    location_context = {
                        'locations_list':locations_list,
    }
    return render(request, 'list-locations.html', location_context)


def create_location_view(request):
    if request.method == 'POST':
        location_form = LocationCreationForm(request.POST)
        if location_form.is_valid():
            location_obj = location_form.save(commit=False)
            location_obj.created_by = request.user
            location_obj.company = request.user.company
            location_obj.save()
    else:
        location_form = LocationCreationForm()
    location_context = {
                        'location_form':location_form,
    }
    return render(request, 'create-location.html', location_context)


def update_location_view(request):
    if request.method == 'POST':
        location_form = LocationCreationForm(request.POST)
        if location_form.is_valid():
            location_obj = location_form.save(commit=False)
            location_obj.created_by = request.user
            location_obj.company = request.user.company
            location_obj.save()
    else:
        location_form = LocationCreationForm()
    location_context = {
                        'location_form':location_form,
    }
    return render(request, 'create-location.html', location_context)


def delete_location_view(request):
    return redirect('location:list-locations')
