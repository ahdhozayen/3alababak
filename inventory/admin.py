from django.contrib import admin
from inventory.models import *


# Register your models here.
#admin.site.register(product,)
admin.site.register(brand)
admin.site.register(category)
admin.site.register(UOM)
#admin.site.register(item)
#admin.site.register(product_attribute)
admin.site.register(attribute)
#admin.site.register(item_attribute_value)

class item_attribute_valueInline(admin.TabularInline):
    model = item_attribute_value

class product_attributeInline(admin.TabularInline):
    model = product_attribute

class itemInline(admin.TabularInline):
    model = item

@admin.register(item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [

        item_attribute_valueInline,

    ]

@admin.register(product)
class ProductAdmin(admin.ModelAdmin):

    inlines = [
        product_attributeInline,
        itemInline,


    ]
