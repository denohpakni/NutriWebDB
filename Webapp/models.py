from django.db import models
from django.contrib.auth.models import User
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

# Cluent's The Placing an order form
# sample/order status in the database
STATUS = [
    ('Ordered',"Ordered"),
    ('Accepted',"Accepted"),
    ('Recieved',"Recieved"),
    ('Extracted',"Extracted"),
    ('QCd',"QCd"),
    ('Reported',"Reported"),
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
    Order_Number = models.CharField(max_length=50,default='OrderNo',blank=True)
    Date_recieved = models.DateTimeField(auto_now_add=True)
    Client = models.CharField(max_length=256, default='Client name')
    No_of_Samples = models.IntegerField(default=1)
    Sample_Type = models.CharField(max_length=99, null=True)
    Sample_Reciever = models.CharField(max_length=128,blank=True)
    Analyis_Required = models.CharField(choices=Analysis_Types,default='Unknown',max_length=256)
    Remarks = models.TextField()
    Stage = models.CharField(choices=STATUS, default='Ordered',max_length=128)
 

# The User information like address, email, 
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    contact_number = models.IntegerField(null=True)
    birth_date = models.DateField(null=True, blank=True)
    Organisation_name = models.CharField(max_length=500,blank=True)
    Address = models.CharField(max_length=256,blank=True)
    Postcode_or_zip_code = models.CharField(max_length=128,blank=True)
    Town_or_City = models.CharField(max_length=128,blank=True)
    Country = models.CharField(max_length=256)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileInfo.objects.create(user=instance)
    instance.userprofileinfo.save()
