from django.contrib import admin
from account.models import *

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Company)
# class CustomerInline(admin.TabularInline):
#    model = customer
# class SupplierInline(admin.TabularInline):
#    model = supplier
# class AddressInline(admin.TabularInline):
#    model = address
#
# class CompanyAdmin(admin.ModelAdmin):
#
#     inlines = [
#         CustomerInline,
#         SupplierInline,
#
#     ]

#admin.site.register(company,CompanyAdmin)
