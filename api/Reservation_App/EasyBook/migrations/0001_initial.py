# Generated by Django 5.0.4 on 2024-04-14 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=500)),
                ('cuisine_type', models.CharField(max_length=100)),
                ('health_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('price_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReservationSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyBook.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyBook.restaurant')),
            ],
        ),
    ]