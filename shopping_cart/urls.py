from django.conf.urls import url

from .views import (
    add_to_cart,
    order_details,
    delete_from_cart
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^service/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
]