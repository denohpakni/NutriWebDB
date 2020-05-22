For the Nutrition platform for the front-end and back-end.

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

