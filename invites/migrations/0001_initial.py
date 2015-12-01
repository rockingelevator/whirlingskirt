# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=40, default='female', choices=[('none', 'Not specified'), ('male', 'Male'), ('female', 'Female')])),
                ('first_name', models.CharField(max_length=255, blank=True, null=True)),
                ('last_name', models.CharField(max_length=255, blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvitedMember',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_of_joining', models.DateTimeField()),
                ('author', models.ForeignKey(related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('invitee', models.ForeignKey(related_name='invitees', to=settings.AUTH_USER_MODEL)),
                ('service_provider', models.ForeignKey(blank=True, null=True, to='accounts.ServiceProvider')),
            ],
        ),
    ]
