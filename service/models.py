from django.db import models

# Create your models here.

class ServiceDetails(models.Model):
    owner_id = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    rent_amount = models.IntegerField()
