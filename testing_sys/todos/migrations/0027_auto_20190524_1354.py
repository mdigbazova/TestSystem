# Generated by Django 2.2 on 2019-05-24 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0026_auto_20190524_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 24, 10, 54, 19, 997171, tzinfo=utc)),
        ),
    ]
