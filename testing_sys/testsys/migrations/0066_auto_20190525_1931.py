# Generated by Django 2.2 on 2019-05-25 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0065_auto_20190525_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 25, 16, 31, 32, 914711, tzinfo=utc), null=True, verbose_name='Alert Timestamp'),
        ),
    ]
