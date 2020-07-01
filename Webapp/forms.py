from django import forms
from django.forms import ModelForm
from Webapp.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('first_name','last_name','email','message')

