import datetime
from datetime import timedelta

# https://djangoproject.com

from django.db import models
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


#  1 cat -------> Many conf
#  1 conf ------> 1 cat:


class Conference(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    venue = models.CharField(max_length=200)
    entry_fee = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    ) # 9999.00
    additional_fee = MoneyField(max_digits=6, decimal_places=2, default_currency='USD', default=0)
    conf_logo = models.ImageField(upload_to='conferences/logo/', null=True)

    class Meta:
        verbose_name = 'Conference'
        verbose_name_plural = 'Conferences'

    def __str__(self):
        return f"{self.title} - {self.category}"
