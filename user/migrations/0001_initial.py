# Generated by Django 5.1.7 on 2025-04-06 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettingmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_server', models.CharField(max_length=100)),
                ('smtp_port', models.IntegerField()),
                ('smtp_username', models.CharField(max_length=100)),
                ('smtp_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoleUserModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url_logo', models.URLField(blank=True, null=True)),
                ('app_setting', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.appsettingmodels')),
            ],
        ),
        migrations.CreateModel(
            name='UserModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('pseudo', models.CharField(max_length=50, unique=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.schoolmodels')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
