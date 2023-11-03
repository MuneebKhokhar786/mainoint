# Generated by Django 4.2.6 on 2023-11-02 01:16

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_shop', '0008_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='laptop_shop.product')),
            ],
        ),
    ]
