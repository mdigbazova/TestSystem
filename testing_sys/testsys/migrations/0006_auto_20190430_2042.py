# Generated by Django 2.2 on 2019-04-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0005_auto_20190430_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsversion',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]