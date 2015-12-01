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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=7)),
                ('currency', models.CharField(default='eur', choices=[('eur', 'EUR'), ('usd', 'USD'), ('uah', 'UAH')], max_length=3)),
                ('transaction_date', models.DateTimeField()),
                ('service_provider', models.ForeignKey(to='accounts.ServiceProvider')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('currency', models.CharField(default='eur', choices=[('eur', 'EUR'), ('usd', 'USD'), ('uah', 'UAH')], max_length=3)),
                ('transaction_date', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
