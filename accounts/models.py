from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from utils import transactions

GENDERS =(
    ('none', 'Not specified'),
    ('male', 'Male'),
    ('female', 'Female')
)


# class Account(models.Model):
#     user = models.OneToOneField(User)
#     gender = models.CharField(max_length=40, choices=GENDERS, default='none')
#     currency = models.CharField(max_length=3, choices=transactions.CURRENCIES, default="eur")
#     balance = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, default=0)
#     total_revenue = models.FloatField(null=True, blank=True, default=0)
#     invited_by = models.ForeignKey(User, blank=True, null=True, related_name='invitee')
#
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, first_name='', last_name='', invited_by=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            invited_by=invited_by,
            registration_date=timezone.now(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=40, choices=GENDERS, default='none')
    invited_by = models.ForeignKey("self", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    registration_date = models.DateTimeField()

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return "%s %s, %s" % (self.first_name, self.last_name, self.email)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class ServiceProvider(models.Model):
    owner = models.ForeignKey(Account)
    name = models.CharField(max_length=255)
    registration_date = models.DateField()

    def __str__(self):
        return self.name


