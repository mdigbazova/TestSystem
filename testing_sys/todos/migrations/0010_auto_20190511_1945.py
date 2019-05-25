# Generated by Django 2.2 on 2019-05-11 16:45

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_auto_20190511_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='state',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'TO BE DONE'), (2, 'PROCESSING'), (3, 'RESEARCHING'), (4, 'FAILED'), (5, 'FIXED'), (6, 'DONE!')], default=1, max_length=11),
        ),
        migrations.AlterField(
            model_name='todo',
            name='style',
            field=models.CharField(choices=[('abap', 'abap'), ('algol', 'algol'), ('algol_nu', 'algol_nu'), ('arduino', 'arduino'), ('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful'), ('default', 'default'), ('emacs', 'emacs'), ('friendly', 'friendly'), ('fruity', 'fruity'), ('igor', 'igor'), ('lovelace', 'lovelace'), ('manni', 'manni'), ('monokai', 'monokai'), ('murphy', 'murphy'), ('native', 'native'), ('paraiso-dark', 'paraiso-dark'), ('paraiso-light', 'paraiso-light'), ('pastie', 'pastie'), ('perldoc', 'perldoc'), ('rainbow_dash', 'rainbow_dash'), ('rrt', 'rrt'), ('tango', 'tango'), ('trac', 'trac'), ('vim', 'vim'), ('vs', 'vs'), ('xcode', 'xcode')], default='solarized-light', max_length=100),
        ),
    ]