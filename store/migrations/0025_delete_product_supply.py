# Generated by Django 5.0.3 on 2024-03-18 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_delete_product_supply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_Supply',
        ),
    ]