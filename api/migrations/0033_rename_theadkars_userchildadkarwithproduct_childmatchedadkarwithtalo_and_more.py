# Generated by Django 4.1.2 on 2023-01-01 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_alter_userchildadkarwithproduct_theadkars_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userchildadkarwithproduct',
            old_name='theAdkars',
            new_name='childMatchedAdkarWithTalo',
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 1, 18, 57, 54, 203111)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 3, 18, 57, 54, 203111)),
        ),
    ]
