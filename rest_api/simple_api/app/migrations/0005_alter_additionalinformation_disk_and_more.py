# Generated by Django 4.1 on 2022-09-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_additionalinformation_disk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinformation',
            name='disk',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='additionalinformation',
            name='network',
            field=models.JSONField(default=dict),
        ),
    ]
