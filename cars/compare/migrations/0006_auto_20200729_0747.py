# Generated by Django 3.0.8 on 2020-07-29 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0005_car_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Emission', models.CharField(blank=True, max_length=100)),
                ('Engine', models.CharField(blank=True, max_length=100)),
                ('cylinder', models.CharField(blank=True, max_length=100)),
                ('Mileage', models.CharField(blank=True, max_length=100)),
                ('Power', models.CharField(blank=True, max_length=100)),
                ('speed', models.CharField(blank=True, max_length=100)),
                ('Gear', models.CharField(blank=True, max_length=100)),
                ('ABS', models.CharField(blank=True, max_length=100)),
                ('Price', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='car',
        ),
    ]