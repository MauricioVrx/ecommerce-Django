# Generated by Django 5.0.3 on 2024-03-15 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_image',
            new_name='category_image',
        ),
    ]
