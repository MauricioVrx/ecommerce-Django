# Generated by Django 5.0.3 on 2024-03-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_rename_colors_product_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='photos/products/<django.db.models.fields.CharField>/main'),
        ),
    ]
