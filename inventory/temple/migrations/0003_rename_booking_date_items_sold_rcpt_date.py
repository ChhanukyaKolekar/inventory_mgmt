# Generated by Django 4.2.7 on 2024-03-22 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temple', '0002_items_sold_rcpt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items_sold_rcpt',
            old_name='Booking_Date',
            new_name='Date',
        ),
    ]
