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
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('value', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('eur', 'EUR'), ('usd', 'USD'), ('uah', 'UAH')], default='eur', max_length=3)),
                ('transaction_date', models.DateTimeField()),
                ('service_provider', models.ForeignKey(to='accounts.ServiceProvider')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('value', models.FloatField()),
                ('currency', models.CharField(choices=[('eur', 'EUR'), ('usd', 'USD'), ('uah', 'UAH')], default='eur', max_length=3)),
                ('transaction_date', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
