# Generated by Django 2.2 on 2019-05-24 11:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testsys', '0035_auto_20190524_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agent',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alertsbody',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts_bodies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsdate',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 11, 18, 30, 610424, tzinfo=utc), null=True, verbose_name='Current Definitions Date'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 11, 18, 30, 611421, tzinfo=utc), verbose_name='Alert Timestamp'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 24, 11, 18, 30, 611421, tzinfo=utc), verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
    ]
