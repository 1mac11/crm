from django.db import models
from company.models import Company
from accounts.models import User


class Location(models.Model):
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=70)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class LocationImages(models.Model):
    title = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
