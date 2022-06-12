from django.db import models


# Create your models here.
class Company(models.Model):
    type_choice = [("Hydropower", "Hydropower"), ("Finance", "Finance"), ("Microfinance", "Micro-Finance"),
                   ("Dev. Banks", "Developement Banks")]
    name = models.CharField(max_length=500)
    type = models.CharField(choices=type_choice, max_length=50)
    abbreviation = models.CharField(max_length=10)
    date_updated = models.DateField(auto_now=True)
    opening = models.IntegerField()
    closing = models.IntegerField()
    transactions = models.BigIntegerField()