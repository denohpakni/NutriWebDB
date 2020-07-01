from django.contrib import admin
from accounts.models import PlaceOrderModel, AddProductModel
# Register your models here.

class PlacedOrdersList(admin.ModelAdmin):
    list_display = ('order_by','product_name','product_quantity','product_price','product_status')

admin.site.register(PlaceOrderModel, PlacedOrdersList)

class producList(admin.ModelAdmin):
    list_display = ('product_name','product_description','product_price','product_category')

admin.site.register(AddProductModel,producList)