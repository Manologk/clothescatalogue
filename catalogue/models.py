from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    price = models.CharField(max_length=10, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
