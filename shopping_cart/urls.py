from django.conf.urls import url
from django.urls import path

from .views import (
    add_to_cart,
    order_details,
    delete_from_cart,
    update_item_number,
    export,
    
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^service/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^service/update/(?P<item_id>[-\w]+)/(?P<item_number>[-\w]+)/$', update_item_number, name='update_item'),
    path('export/',export,name='export'),

    
]