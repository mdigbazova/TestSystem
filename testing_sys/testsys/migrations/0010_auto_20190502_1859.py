# Generated by Django 2.2 on 2019-05-02 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0009_auto_20190501_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertsbody',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='testsys.Account'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='testsys.Agent'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('likes', models.PositiveIntegerField()),
                ('dislikes', models.PositiveIntegerField()),
                ('alerts_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='testsys.AlertsBody')),
                ('author', models.ForeignKey(default='Anonymous', max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='testsys.Profile')),
            ],
        ),
    ]