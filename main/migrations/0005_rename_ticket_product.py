# Generated by Django 5.0.3 on 2024-03-25 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_ticket_create_date_ticket_update_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ticket',
            new_name='Product',
        ),
    ]