from django.db import models
from django.contrib.auth.models import User
from utils import transactions
from accounts.models import ServiceProvider


class Booking(models.Model):
    user = models.ForeignKey(User)
    service_provider = models.ForeignKey(ServiceProvider)
    value = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default="eur")
    transaction_date = models.DateTimeField()

    def __str__(self):
        return "%s %s: %s %f" % (self.user.first_name,
                                 self.user.last_name,
                                 self.currency,
                                 self.value)


class Payment(models.Model):
    user = models.ForeignKey(User)
    value = models.FloatField()
    currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default='eur')
    transaction_date = models.DateTimeField()

    def __str__(self):
        return "%s %f to %s %s at %s" % (self.currency,
                                         self.value,
                                         self.user.first_name,
                                         self.user.last_name,
                                         str(self.transaction_date))