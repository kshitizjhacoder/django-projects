# Generated by Django 4.1.3 on 2023-01-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpro', '0002_remove_reservation_cld_reservation_seat_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amt',
            field=models.IntegerField(default=0),
        ),
    ]