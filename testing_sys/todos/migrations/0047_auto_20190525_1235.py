# Generated by Django 2.2 on 2019-05-25 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0046_auto_20190525_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 25, 9, 35, 54, 229393, tzinfo=utc)),
        ),
    ]
