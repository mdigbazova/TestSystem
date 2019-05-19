# Generated by Django 2.2 on 2019-05-19 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0024_auto_20190519_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 11, 12, 41, 822629, tzinfo=utc), verbose_name='Current Definitions Date'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 11, 12, 41, 822629, tzinfo=utc), verbose_name='Alert Timestamp'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 19, 11, 12, 41, 822629, tzinfo=utc), verbose_name='Creation Date'),
        ),
    ]
