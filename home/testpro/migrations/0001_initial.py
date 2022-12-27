# Generated by Django 4.1.3 on 2022-12-25 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('email', models.EmailField(max_length=25, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('phone', models.BigIntegerField(default=91, unique=True)),
                ('street', models.CharField(default='something', max_length=40)),
                ('city', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('bday', models.IntegerField()),
                ('bmonth', models.CharField(default='januwary', max_length=10)),
                ('byear', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.IntegerField(primary_key=True, serialize=False)),
                ('station_name', models.CharField(max_length=30)),
                ('station_platforms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('class_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Source', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('PNR', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name_of_train', models.CharField(max_length=30)),
                ('no_of_coach', models.IntegerField(default=0)),
                ('no_of_seats_in_general', models.IntegerField(default=0)),
                ('no_of_seats_in_Sleeper', models.IntegerField(default=0)),
                ('no_of_seats_in_AC', models.IntegerField(default=0)),
                ('dept_time', models.TimeField()),
                ('dept_date', models.DateField()),
                ('arriv_time', models.TimeField()),
                ('arriv_date', models.DateField()),
                ('times', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpro.timing')),
            ],
        ),
        migrations.CreateModel(
            name='Seat_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.CharField(max_length=10)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpro.train')),
            ],
        ),
    ]