from decimal import Decimal
from django.db import models
from accounts.models import Account
from utils.transactions import CURRENCIES, BONUSES
from accounts.models import ServiceProvider


class Booking(models.Model):
    account = models.ForeignKey(Account)
    service_provider = models.ForeignKey(ServiceProvider)
    value = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default="eur")
    transaction_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        # give bonus for user who invited this account
        if self.account.invited_by is not None:
            member_bonus = self.value * BONUSES['commission']['from_booking'] / 100 if self.value < BONUSES['for']['member'] else BONUSES['commission']['from_provision'] * BONUSES['for']['member'] / 100
            print('Member bonus', member_bonus)
            try:
                balance = Balance.objects.get(account=self.account.invited_by)
            except Balance.DoesNotExist:
                # balance has not been created yet, do it now
                balance = Balance(account=self.account.invited_by, current_balance=member_bonus)
            else:
                balance.current_balance += Decimal(member_bonus)
            finally:
                balance.save()
        # give bonus for user who invited service provider's owner
        if self.service_provider.owner.invited_by is not None:
            bonus_account = self.service_provider.owner.invited_by
            if self.account != self.service_provider.owner and self.account.invited_by != bonus_account:
                # if user is also a owner of this institute then there is no bonus for institute
                # or if its the same person who invites this user and this SP
                sp_bonus = self.value * BONUSES['commission']['from_booking'] / 100 if self.value < BONUSES['for']['sp'] else BONUSES['commission']['from_provision'] * BONUSES['for']['sp'] / 100
                print('sp_bonus', sp_bonus)
                try:
                    balance = Balance.objects.get(account=bonus_account)
                except Balance.DoesNotExist:
                    # balance has not been created yet, do it now
                    balance = Balance(account=bonus_account, current_balance=sp_bonus)
                else:
                    balance.current_balance += Decimal(sp_bonus)
                finally:
                    balance.save()
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s: %s %.2f" % (self.account.first_name,
                                 self.account.last_name,
                                 self.currency,
                                 self.value)


class Payment(models.Model):
    account = models.ForeignKey(Account)
    value = models.DecimalField(max_digits=7, decimal_places=2, )
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='eur')
    transaction_date = models.DateTimeField()

    def __str__(self):
        return "%s %.2f to %s %s at %s" % (self.currency,
                                         self.value,
                                         self.account.first_name,
                                         self.account.last_name,
                                         str(self.transaction_date))


class Balance(models.Model):
    account = models.ForeignKey(Account)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default="eur")
    current_balance = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "%s %s: %.2f %s" % (self.account.first_name,
                                   self.account.last_name,
                                   self.current_balance,
                                   self.currency)