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
