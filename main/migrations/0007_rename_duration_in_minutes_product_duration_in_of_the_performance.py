# Generated by Django 5.0.2 on 2024-04-01 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_duration_in_minutes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='duration_in_minutes',
            new_name='duration_in_of_the_performance',
        ),
    ]