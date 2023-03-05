# Generated by Django 4.1.2 on 2022-11-22 11:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_shikhcategory_simdesc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=255)),
                ('bookingPrice', models.FloatField(default=5)),
            ],
        ),
        migrations.AlterField(
            model_name='shikhcategory',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/shikh'),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 22, 14, 35, 21, 321702)),
        ),
        migrations.AlterField(
            model_name='userproductsroutine',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2022, 11, 24, 14, 35, 21, 321702)),
        ),
        migrations.CreateModel(
            name='DoctorAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAssignedDated', models.DateTimeField()),
                ('doctorAssignedDated', models.DateTimeField()),
                ('sessionEnded', models.BooleanField(default=False)),
                ('userRate', models.IntegerField(default=3)),
                ('theCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.appointmentcategory')),
                ('theUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
        ),
    ]
