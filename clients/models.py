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


APPLICATION_STATUS = (
    ("accepted", "accepted"),
    ("screening", "screening"),
    ("rejected", "rejected"),
    ("received", "received"),
    ("on_process", "on_process"),
    ("ready", "ready"),
)


class Application(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    deadline = models.DateTimeField()
    status = models.CharField(choices=APPLICATION_STATUS, max_length=10)

    def __str__(self):
        return str(self.client) + 'wants to buy' + self.product.name
