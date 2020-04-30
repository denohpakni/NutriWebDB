from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# The contact form from the client
class Message(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email

# Cluent's The Placing an order form
# sample/order status in the database
STATUS = [
    (0,"Ordered"),
    (1,"Accepted"),
    (2,"Recieved"),
    (3,"Extracted"),
    (4,"QCd"),
    (5,"Reported"),
]

Analysis_Types = [
    ('Unknown','Unknown'),
    ('Sample Milling','Sample Milling'),
    ('Protein','Protein'),
    ('Aflatoxin','Aflatoxin'),
    ('Multimycotoxin','Multimycotoxin'),
    ('Primary Amino Acids','Primary Amino Acids'),
    ('Water soluble vitamin','Water soluble vitamin'),
    ('Fat soluble vitamins','Fat soluble vitamins'),
    ('Tannins','Tannins'),
    ('DM content','DM content'),
]

class Order(models.Model):
    Order_Number = models.CharField(primary_key=True,max_length=50,default='OrderNo',unique=True,blank=True)
    Date_recieved = models.DateTimeField(auto_now_add=True)
    Client = models.CharField(max_length=256, default='Client name')
    No_of_Samples = models.IntegerField(default=1)
    Sample_Type = models.CharField(max_length=99, null=True)
    Sample_Reciever = models.CharField(max_length=128,blank=True)
    Analyis_Required = models.CharField(choices=Analysis_Types,default='Unknown',max_length=256)
    Remarks = models.TextField()
    Stage = models.IntegerField(choices=STATUS, default=0)
 

# The User information like address, email, 
class UserProfileInfo(models.Model):
    name = models.CharField(default=User,max_length=256)
    contact_number = models.PositiveIntegerField()
    Organisation_name = models.TextField(blank=True)
    Address = models.CharField(max_length=128,blank=True)
    Town_or_City = models.CharField(max_length=128,blank=True)
    Postcode_or_zip_code = models.CharField(max_length=128,blank=True)
    Country = models.CharField(max_length=128)
