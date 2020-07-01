from django.forms import ModelForm
from .models import AddProductModel
# from .models import PlaceOrderModel


class AddProductForm(ModelForm):
    class Meta:
        model = AddProductModel
        fields = '__all__'


# class PlaceOrderForm(ModelForm):
#     class Meta:
#         model = PlaceOrderModel
#         fields = ['product_quantity']
