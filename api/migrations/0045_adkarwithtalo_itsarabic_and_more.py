# Generated by Django 4.1.2 on 2023-01-27 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_appinformation_fmlink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adkarwithtalo',
            name='itsArabic',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 27, 14, 20, 23, 245918)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 29, 14, 20, 23, 245918)),
        ),
    ]
