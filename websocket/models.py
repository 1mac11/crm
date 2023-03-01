from django.db import models
from company.models import Company


# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    read_status = models.BooleanField(blank=True, default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
