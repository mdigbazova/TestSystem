# Generated by Django 2.2 on 2019-05-23 09:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0029_auto_20190519_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 9, 29, 38, 642025, tzinfo=utc), null=True, verbose_name='Current Definitions Date'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 9, 29, 38, 642025, tzinfo=utc), verbose_name='Alert Timestamp'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 23, 9, 29, 38, 642025, tzinfo=utc), verbose_name='Creation Date'),
        ),
    ]
