# Generated by Django 3.0.6 on 2020-08-01 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
