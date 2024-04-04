# Generated by Django 5.0.2 on 2024-04-04 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_play_remove_product_age_limit_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Play',
            new_name='Performance',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='main.performance', verbose_name='Билет спектакля'),
            preserve_default=False,
        ),
    ]
