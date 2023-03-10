# Generated by Django 4.1.3 on 2023-01-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockValues', '0002_alter_pnl_deprication_alter_pnl_expense_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='dividend',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='price',
            name='high',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='price',
            name='low',
            field=models.FloatField(default=0.0),
        ),
    ]
