from django.db import models

from accounts.models import User
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_owner',
                              verbose_name=_('company_owner'))
    phone = models.CharField(_('phone'), max_length=20)
    email = models.EmailField(_('email'), unique=True)
    employee = models.ManyToManyField(User, related_name='employee', verbose_name=_('employee'))
    logo = models.ImageField(_('logo'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _("Companies")


class Product(models.Model):
    name = models.CharField(unique=True, max_length=30, verbose_name=_('product name'))
    price = models.DecimalField(decimal_places=2, max_digits=20, verbose_name=_('price'))
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name=_('company'))
    image = models.ImageField(blank=True, null=True, verbose_name=_('image'))
    count = models.IntegerField(verbose_name=_('count'))
    available = models.BooleanField(default=False, verbose_name=_('available'))

    def __str__(self):
        return self.name
