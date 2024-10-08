# Generated by Django 4.1.2 on 2023-10-10 14:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_orderedproduct_isfrombug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 10, 10, 17, 21, 23, 337162)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 10, 12, 17, 21, 23, 338156)),
        ),
        migrations.CreateModel(
            name='SendNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('desc', models.CharField(default='', max_length=255)),
                ('isLocalNotification', models.BooleanField(default=False)),
                ('number', models.IntegerField(default=0)),
                ('theUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
    ]
