from django import forms
from django.forms import ModelForm
from Webapp.models import Message, Order, UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('first_name','last_name','email','message')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('Client','No_of_Samples','Sample_Type','Analyis_Required','Remarks')


##############################
##### User Profile info #####
##############################

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta():
        model = User
        fields = ('first_name','last_name','username','password1','password2','email')
        
class UserProfileInfoForm(ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta():
        model = UserProfileInfo
        fields = ('first_name','last_name','email','contact_number','birth_date','Organisation_name','Address','Town_or_City','Postcode_or_zip_code','Country')


########## A Simple but Complex Form ###############

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

