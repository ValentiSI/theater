# Generated by Django 5.0.3 on 2024-04-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_product_product_performance'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название билета'),
            preserve_default=False,
        ),
    ]
