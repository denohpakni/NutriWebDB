from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Webapp.models import Message, Customer,Order, OrderItem, Product

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('first_name','last_name','email','message')

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','password1','password2')

class CustomerForm(ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta():
        model = Customer
        fields = ('first_name','last_name','email','contact_number','birth_date','Organisation_name','Address','Town_or_City','Postcode_or_zip_code','Country')

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('Sample_Type','Remarks')

class OrderItemForm(ModelForm):
	class Meta:
		model= OrderItem
		fields = ('product','quantity')

OrderItemFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm,extra=2)
