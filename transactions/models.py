from django.db import models
from accounts.models import Account
from utils import transactions
from accounts.models import ServiceProvider


class Booking(models.Model):
    account = models.ForeignKey(Account)
    service_provider = models.ForeignKey(ServiceProvider)
    value = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default="eur")
    transaction_date = models.DateTimeField()

    def __str__(self):
        return "%s %s: %s %.2f" % (self.user.first_name,
                                 self.user.last_name,
                                 self.currency,
                                 self.value)


class Payment(models.Model):
    account = models.ForeignKey(Account)
    value = models.DecimalField(max_digits=7, decimal_places=2, )
    currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default='eur')
    transaction_date = models.DateTimeField()

    def __str__(self):
        return "%s %.2f to %s %s at %s" % (self.currency,
                                         self.value,
                                         self.user.first_name,
                                         self.user.last_name,
                                         str(self.transaction_date))


class Balance(models.Model):
    account = models.ForeignKey(Account)
    currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default="eur")
    current_balance = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "%s %s: %.2f %s" % (self.user.first_name,
                                   self.user.last_name,
                                   self.current_balance,
                                   self.currency)