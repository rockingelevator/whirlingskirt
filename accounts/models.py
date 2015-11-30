from django.db import models
from django.contrib.auth.models import User
from utils import transactions

GENDERS =(
    ('none', 'Not specified'),
    ('male', 'Male'),
    ('female', 'Female')
)


class Account(User):
    gender = models.CharField(max_length=40, choices=GENDERS, default='none')
    currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default="eur")
    balance = models.FloatField(null=True, blank=True, default=0)
    total_revenue = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class ServiceProvider(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    registration_date = models.DateField()

    def __str__(self):
        return self.name


