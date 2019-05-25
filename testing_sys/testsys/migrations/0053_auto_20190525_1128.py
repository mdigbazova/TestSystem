# Generated by Django 2.2 on 2019-05-25 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0052_auto_20190524_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 25, 8, 28, 5, 519004, tzinfo=utc), null=True, verbose_name='Current Definitions Date'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 25, 8, 28, 5, 520001, tzinfo=utc), null=True, verbose_name='Alert Timestamp'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='createdat',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 25, 8, 28, 5, 520001, tzinfo=utc), verbose_name='Creation Date'),
        ),
    ]