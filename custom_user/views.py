from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import authenticate
from custom_user.forms import UserForm


# Create your views here.
def register(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form= UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
    reg_form ={'form':user_form}
    return render(request,'register.html',context = reg_form)
