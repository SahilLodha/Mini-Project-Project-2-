from django.db import models


# Create your models here.
class Company(models.Model):
    type_choice = [("Hydropower", "Hydropower"), ("Finance", "Finance"), ("Microfinance", "Micro-Finance"),
                   ("Dev. Banks", "Developement Banks")]
    name = models.CharField(max_length=500)
    type = models.CharField(choices=type_choice, max_length=50, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    date_updated = models.DateField(auto_now=True)
    max = models.IntegerField()
    min = models.IntegerField()
    closing = models.IntegerField()
    previous_closing = models.IntegerField()