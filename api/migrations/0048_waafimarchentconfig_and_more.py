# Generated by Django 4.1.2 on 2023-02-22 07:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_listeningcilajwithquran_isvideo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaafiMarchentConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchantUid', models.CharField(default='', max_length=255)),
                ('apiUserId', models.CharField(default='', max_length=255)),
                ('apiKey', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='listeningcilajwithquran',
            name='theShikh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dhagaysigaWithMuqaalkaShiiqa', to='api.shikhcategory'),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2023, 2, 22, 10, 35, 21, 320224)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2023, 2, 24, 10, 35, 21, 321223)),
        ),
    ]
