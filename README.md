For the Nutrition platform for the front-end and back-end.

## Requirements

asgiref==3.2.7
astroid==2.4.1
beautifulsoup4==4.9.1
colorama==0.4.3
Django==3.0.6
django-adminlte3==0.1.6
django-bootstrap4==1.1.1
django-countries==6.1.2
django-gunicorn==0.1.1
gunicorn==20.0.4
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
pylint==2.5.2
pytz==2020.1
six==1.15.0
soupsieve==2.0.1
sqlparse==0.3.1
toml==0.10.1
whitenoise==5.1.0
wrapt==1.12.1


## Achievements; 
> 12/5/20 
1. Figured out how to avail a navbar only to a Staff user to view database
2. Was able to add a profile to a new signing up user
3. 

## Challenges yet to overcome
> 12/5/20
1. Cant link a logged in user to make an entry into the database .e.g logged in user to record their sales for the day
2. Categorising of the Products while making an order
3. Admin doesnt require a Profile to login

   C:\Users\DMwangi\Documents\NutriWebDB\Webapp\models.py in update_user_profile
       Country = models.CharField(max_length=256)
   @receiver(post_save, sender=User)
   def update_user_profile(sender, instance, created, **kwargs):
       if created:
           UserProfileInfo.objects.create(user=instance)
       instance.userprofileinfo.save() 

