from django.contrib import admin
from account.models import supplier,customer,company,address

# Register your models here.
admin.site.register(supplier)
admin.site.register(customer)
admin.site.register(address)
admin.site.register(company)
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
