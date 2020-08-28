from django.db import models

from Webapp.models import Services
from Webapp.models import Profile

class ServiceItem(models.Model):
    service = models.ForeignKey(Services, on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    number_of_samples= models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered= models.DateTimeField(null=True)

    def __str__(self):
        return self.service.description

class OrderServices(models.Model):
    ref_code= models.CharField(max_length=15)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(ServiceItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)



