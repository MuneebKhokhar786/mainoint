# Generated by Django 4.2.6 on 2024-04-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_shop', '0014_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
