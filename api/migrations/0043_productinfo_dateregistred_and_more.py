# Generated by Django 4.1.2 on 2023-01-27 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_alter_doctorappointment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='dateRegistred',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 27, 11, 8, 24, 55909)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 29, 11, 8, 24, 55909)),
        ),
    ]
