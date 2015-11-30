# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('gender', models.CharField(max_length=40, default='none', choices=[('none', 'Not specified'), ('male', 'Male'), ('female', 'Female')])),
                ('currency', models.CharField(max_length=3, default='eur', choices=[('eur', 'EUR'), ('usd', 'USD'), ('uah', 'UAH')])),
                ('balance', models.FloatField(null=True, default=0, blank=True)),
                ('total_revenue', models.FloatField(null=True, default=0, blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('registration_date', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
