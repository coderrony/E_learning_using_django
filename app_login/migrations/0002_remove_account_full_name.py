# Generated by Django 4.2.4 on 2023-08-22 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='full_name',
        ),
    ]