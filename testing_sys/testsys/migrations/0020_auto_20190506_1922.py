# Generated by Django 2.2 on 2019-05-06 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0019_auto_20190506_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsbody',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_to_alerts_body', to='testsys.Account', verbose_name='Object Account'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_to_alerts_body', to='testsys.Agent', verbose_name='Object Agent'),
        ),
    ]
