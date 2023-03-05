# Generated by Django 4.1.2 on 2022-11-26 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_doctorappointment_doctorassigneddated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentcategory',
            name='fullDesc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 26, 15, 52, 38, 556923)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 28, 15, 52, 38, 556923)),
        ),
    ]
