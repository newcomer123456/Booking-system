# Generated by Django 5.0.7 on 2024-08-01 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Availability',
        ),
    ]
