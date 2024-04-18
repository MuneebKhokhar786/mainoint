# Generated by Django 4.2.6 on 2024-04-18 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_shop', '0020_branch_created_at_branch_updated_at_and_more'),
        ('inventory', '0002_localinventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localinventory',
            name='product',
        ),
        migrations.AddField(
            model_name='globalinventory',
            name='product',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='laptop_shop.product'),
        ),
    ]
