from django.db import models
from company.models import Company
from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    name = models.CharField(max_length=15, verbose_name=_('name'))
    address = models.CharField(max_length=70, verbose_name=_('address'))
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_('location company'))
    employee = models.ManyToManyField(User, verbose_name=_('employee'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class LocationImages(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name=_('location'))
    image = models.ImageField(upload_to='', verbose_name=_('image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Location Image')
        verbose_name_plural = _('Location Images')
