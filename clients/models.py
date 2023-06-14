from django.db import models
from company.models import Product, Company


class Clients(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20, blank=True, null=True)
    bought_products = models.ManyToManyField(Product, blank=True, null=True, related_name='bought_products')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name + self.surname
