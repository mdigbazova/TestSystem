# Generated by Django 2.2 on 2019-05-19 19:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0021_auto_20190519_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 19, 19, 48, 34, 939880, tzinfo=utc)),
        ),
    ]
