from django import forms
from Webapp.models import Message, Order

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('first_name','last_name','email','message')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('Client','Client_Address','Sample_Type','Analyis_Required','Remarks')
