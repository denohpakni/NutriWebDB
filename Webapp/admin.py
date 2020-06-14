from django.contrib import admin
from Webapp.models import Message, Customer
from django.contrib.auth.models import User
from Webapp.models import Category, Product, OrderItem, Order
# Register your models here.


# Change Admin Title and Header
admin.site.site_title = "DB"
admin.site.site_header = "Nutrition Platform DataBase"
admin.site.index_title = "DB page-Welcome!"


# ModelAdmin Class is a representation of user-defined models in the admin panel.
# We have to register the Admin Model alongside the model we want to change. 
# This class is used to override the default class views. 

class CustomerList(admin.ModelAdmin):
    fields = ['Client','first_name','last_name','email','contact_number','birth_date','Organisation_name','Address','Town_or_City','Postcode_or_zip_code','Country']
    list_display = ['first_name','last_name','Organisation_name','Country']
    search_fields = ['User','first_name','last_name','Organisation_name','Country']

admin.site.register(Customer, CustomerList)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    filter_horizontal = ("product",)


# Register your models after describing them.

admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
