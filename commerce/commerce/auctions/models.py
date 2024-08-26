import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class GenericModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    created_at = models.DateTimeField(auto_now=datetime.datetime.now())

    class Meta:
        abstract = True

class Category(GenericModel):
    name = models.CharField(max_length=20)

class Listings(GenericModel):

    title = models.CharField(null=False, blank=False, max_length=150)
    details = models.TextField()
    min_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image_url = models.TextField()
    is_closed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Bids(GenericModel):
    
    listing = models.ForeignKey(Listings, null=False, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    

class Comments(GenericModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    comment = models.TextField()


