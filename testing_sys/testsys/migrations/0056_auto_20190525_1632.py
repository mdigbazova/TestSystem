# Generated by Django 2.2 on 2019-05-25 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0055_auto_20190525_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 25, 13, 32, 48, 732165, tzinfo=utc), null=True, verbose_name='Alert Timestamp'),
        ),
    ]
