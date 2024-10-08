# Generated by Django 4.1.2 on 2022-11-27 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_appointmentcategory_fulldesc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='isRoutine',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='theUsageTimes',
            field=models.ManyToManyField(blank=True, null=True, to='api.routinetime'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='latestMonthAnsweredQuestion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 27, 19, 49, 52, 873439)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='isRoutine',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 29, 19, 49, 52, 873439)),
        ),
    ]
