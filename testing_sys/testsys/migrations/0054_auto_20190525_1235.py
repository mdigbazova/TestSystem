# Generated by Django 2.2 on 2019-05-25 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0053_auto_20190525_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsdate',
            field=models.DateField(auto_now=True, null=True, verbose_name='Current Definitions Date'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 25, 9, 35, 54, 212441, tzinfo=utc), null=True, verbose_name='Alert Timestamp'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='createdat',
            field=models.DateField(auto_now=True, verbose_name='Creation Date'),
        ),
    ]
