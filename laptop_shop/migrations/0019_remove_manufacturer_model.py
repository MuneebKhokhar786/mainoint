# Generated by Django 4.2.6 on 2024-04-06 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_shop', '0018_manufacturer_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='model',
        ),
    ]
