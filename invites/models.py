from django.db import models
from django.contrib.auth.models import User
from accounts.models import ServiceProvider, GENDERS


class Invite(models.Model):
    author = models.ForeignKey(User)
    email = models.EmailField()
    gender = models.CharField(max_length=40, choices=GENDERS, default="female")
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    creation_date = models.DateTimeField()

    def __str__(self):
        return "%s %s sent invite to %s" % (self.author.first_name,
                                            self.author.last_name,
                                            self.email)


class InvitedMember(models.Model):
    author = models.ForeignKey(User, related_name='authors')
    invitee = models.ForeignKey(User, related_name='invitees')
    service_provider = models.ForeignKey(ServiceProvider, null=True, blank=True)
    date_of_joining = models.DateTimeField()

    def __str__(self):
        output = "%s %s invited by %s %s" % (self.author.first_name,
                                                     self.author.last_name,
                                                     self.invitee.first_name,
                                                     self.invitee.last_name)
        if(self.service_provider):
            output = ', '.join([self.service_provider.name, output])
        return output


