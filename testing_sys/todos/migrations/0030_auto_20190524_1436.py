# Generated by Django 2.2 on 2019-05-24 11:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0029_auto_20190524_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 24, 11, 36, 28, 787034, tzinfo=utc)),
        ),
    ]