# Generated by Django 2.2 on 2019-05-02 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0010_auto_20190502_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='testsys.Profile'),
        ),
    ]
