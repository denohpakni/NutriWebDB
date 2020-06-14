from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# The contact form from the client
class Message(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email

class Customer(models.Model):
	User= settings.AUTH_USER_MODEL
	Client = models.ForeignKey(User,null=True,on_delete = models.CASCADE)
	first_name = models.CharField(max_length=60, blank=True)
	last_name = models.CharField(max_length=60, blank=True)
	email = models.EmailField(max_length=100, blank=True)
	contact_number = models.IntegerField(null=True)
	birth_date = models.DateField(null=True, blank=True)
	Organisation_name = models.CharField(max_length=500,blank=True)
	Address = models.CharField(max_length=256,blank=True)
	Postcode_or_zip_code = models.CharField(max_length=128,blank=True)
	Town_or_City = models.CharField(max_length=128,blank=True)
	Country = CountryField(blank_label='(select country)')
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name


class Category(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = [
		('Ordered','Ordered'),
		('Accepted',"Accepted"),
		('Recieved',"Recieved"),
		('Extracted',"Extracted"),
		('QCd',"QCd"),
		('Complete',"Complete"),
	]
	
	Order_Number = models.CharField(max_length=100,default='01234')
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)	
	Sample_Type = models.CharField(max_length=99, null=True)
	Remarks = models.TextField()
	Sample_Reciever = models.CharField(max_length=128,blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='Ordered')
	
	def __str__(self):
		return self.Order_Number

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ManyToManyField(Product)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.order
