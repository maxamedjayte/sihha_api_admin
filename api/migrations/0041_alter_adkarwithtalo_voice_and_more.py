# Generated by Django 4.1.2 on 2023-01-25 16:00

import cloudinary_storage.storage
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_alter_userproductsroutine_fromdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adkarwithtalo',
            name='voice',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='voice/adkarWithTalo/'),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 25, 19, 0, 28, 751528)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 1, 27, 19, 0, 28, 751528)),
        ),
    ]
