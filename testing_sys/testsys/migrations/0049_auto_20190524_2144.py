# Generated by Django 2.2 on 2019-05-24 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0048_auto_20190524_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 24, 18, 44, 46, 374313, tzinfo=utc), null=True, verbose_name='Alert Timestamp'),
        ),
    ]