# Generated by Django 4.2.3 on 2023-09-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_shop', '0003_collection_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(null=True, upload_to='laptop_shop/static/laptop_shop/images/collections/'),
        ),
    ]
