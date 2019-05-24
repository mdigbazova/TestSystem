# Generated by Django 2.2 on 2019-05-24 11:43

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0030_auto_20190524_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 24, 11, 43, 48, 416134, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL),
        ),
    ]
