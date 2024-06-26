# Generated by Django 4.2.6 on 2024-04-05 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_shop', '0013_product_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
