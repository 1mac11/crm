from django.db import models

from accounts.models import User


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_owner')
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    employee = models.ManyToManyField(User, related_name='employee')

    def __str__(self):
        return self.name


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
