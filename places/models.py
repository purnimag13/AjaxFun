from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    country = models.ForeignKey(Country)

