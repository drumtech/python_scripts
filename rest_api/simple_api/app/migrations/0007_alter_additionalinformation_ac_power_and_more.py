# Generated by Django 4.1 on 2022-09-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_additionalinformation_ac_power_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinformation',
            name='AC_power',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='battery_charge_percentage',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='cpu',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='disk',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='host_information',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='load_average',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='memory',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='network',
            field=models.JSONField(default=dict),
        ),
    ]
