# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=40, default='female', choices=[('none', 'Not specified'), ('male', 'Male'), ('female', 'Female')])),
                ('first_name', models.CharField(blank=True, null=True, max_length=255)),
                ('last_name', models.CharField(blank=True, null=True, max_length=255)),
                ('message', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvitedMember',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date_of_joining', models.DateTimeField()),
                ('author', models.ForeignKey(related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('invitee', models.ForeignKey(related_name='invitees', to=settings.AUTH_USER_MODEL)),
                ('service_provider', models.ForeignKey(null=True, to='accounts.ServiceProvider', blank=True)),
            ],
        ),
    ]
