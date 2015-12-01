# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('gender', models.CharField(default='none', max_length=40, choices=[('none', 'Not specified'), ('male', 'Male'), ('female', 'Female')])),
                ('currency', models.CharField(default='eur', max_length=3, choices=[('eur', 'EUR'), ('usd', 'USD'), ('uah', 'UAH')])),
                ('balance', models.DecimalField(default=0, max_digits=7, blank=True, null=True, decimal_places=2)),
                ('total_revenue', models.FloatField(default=0, blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
