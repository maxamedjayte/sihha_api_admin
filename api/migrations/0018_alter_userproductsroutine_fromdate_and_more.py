# Generated by Django 4.1.2 on 2022-11-29 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_appinformation_subscriptionbuttondesc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 29, 7, 53, 13, 911443)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2022, 12, 1, 7, 53, 13, 911443)),
        ),
    ]
