# Generated by Django 5.0.3 on 2024-03-18 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_cat_image_category_category_image'),
        ('store', '0033_remove_product_supply_product_delete_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.PositiveIntegerField(blank=True)),
                ('product_image', models.ImageField(blank=True, upload_to='photos/products/<django.db.models.fields.related.ForeignKey>/main')),
                ('description', models.TextField(max_length=700)),
                ('is_active', models.BooleanField(default=False)),
                ('limited', models.IntegerField(default=-1)),
                ('slug', models.CharField(blank=True, max_length=200)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('supply', models.ManyToManyField(to='store.supply')),
                ('tags', models.ManyToManyField(to='store.tag')),
            ],
        ),
    ]
