# Generated by Django 2.2 on 2019-05-11 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_auto_20190511_1945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('owner', 'state')},
        ),
    ]