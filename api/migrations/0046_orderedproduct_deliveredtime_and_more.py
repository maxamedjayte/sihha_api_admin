# Generated by Django 4.1.2 on 2023-01-27 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_adkarwithtalo_itsarabic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproduct',
            name='deliveredTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 27, 15, 25, 8, 473134)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 29, 15, 25, 8, 473134)),
        ),
    ]
