# Generated by Django 2.2 on 2019-05-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0047_auto_20190525_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
