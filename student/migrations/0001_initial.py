# Generated by Django 5.1.7 on 2025-04-06 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absence_date', models.DateField()),
                ('absence_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentCardsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('url_picture', models.URLField()),
                ('gender', models.CharField(choices=[('MEN', 'Men'), ('WOMEN', 'Women'), ('OTHER', 'Other')], max_length=10)),
                ('mailticket', models.CharField(max_length=100)),
                ('phone_number_label', models.CharField(max_length=100)),
                ('classe', models.CharField(max_length=100)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='personn.addressmodels')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
