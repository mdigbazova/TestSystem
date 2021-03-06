# Generated by Django 2.2 on 2019-05-02 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsys', '0014_auto_20190502_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agentid',
            field=models.CharField(max_length=10, verbose_name='Agent ID'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agentstatename',
            field=models.CharField(choices=[('0', 'UNKNOWN'), ('1', 'IDLE'), ('2', 'SCANNING'), ('3', 'SNOOZED'), ('4', 'DEACTIVATED'), ('5', 'DOWNLOADING_ENGINE'), ('6', 'INSTALLING_ENGINE'), ('7', 'ENGINE_INSTALL_FAILED'), ('8', 'UNINSTALLED'), ('9', 'INSTALLING'), ('10', 'INSTALL_COMPLETE'), ('13', 'COMPETETIVE_REMOVAL'), ('14', 'COMPETETIVE_REMOVAL_FAILED'), ('15', 'COMPETETIVE_PRODUCT_DETECTED'), ('16', 'DOWNLOADING_COMPETETIVE_REMOVER'), ('17', 'INSTALLING_COMPETETIVE_REMOVER')], max_length=1, verbose_name='Agent State Name'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agentversion',
            field=models.CharField(max_length=20, verbose_name='Agent Version'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsdate',
            field=models.DateTimeField(verbose_name='Current Definitions Date'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='currentdefinitionsversion',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Current Definitions Version'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='foreigndeviceguid',
            field=models.CharField(max_length=80, verbose_name='Foreign Device GUID'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='policyid',
            field=models.CharField(max_length=10, verbose_name='Policy ID'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='sdkproductversion',
            field=models.CharField(max_length=20, verbose_name='SDK Product Version'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='testsys.Account', verbose_name='Object Account'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='testsys.Agent', verbose_name='Object Agent'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alert_id',
            field=models.CharField(max_length=80, verbose_name='Alert ID'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alertstate',
            field=models.CharField(choices=[('0', 'UNDEFINED'), ('1', 'NEW'), ('2', 'RESOLVED')], max_length=1, verbose_name='Alert State'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='alerttimestamp',
            field=models.DateTimeField(verbose_name='Alert Timestamp'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='createdat',
            field=models.DateTimeField(verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='external_service_id',
            field=models.CharField(choices=[('1', 'AVERY'), ('2', 'BRECK'), ('3', 'ECHO')], max_length=1, verbose_name='External Service ID'),
        ),
        migrations.AlterField(
            model_name='alertsbody',
            name='rm_region',
            field=models.CharField(max_length=15, verbose_name='Remote Region'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='alerts_body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='testsys.AlertsBody', verbose_name='Alerts Body'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='testsys.Profile', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='dislikes',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Dislikes'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Likes'),
        ),
    ]
