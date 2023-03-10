# Generated by Django 4.1.3 on 2023-02-01 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cld',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('amt', models.IntegerField(default=0)),
                ('class_at', models.CharField(max_length=20)),
                ('seat_no', models.CharField(default=None, max_length=5)),
                ('aval', models.CharField(default='TRUE', max_length=10)),
            ],
        ),
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
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=10)),
                ('seat_no', models.CharField(default=None, max_length=5)),
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
                ('Source', models.CharField(default=None, max_length=50)),
                ('Destination', models.CharField(default=None, max_length=50)),
                ('arriv_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnr', models.CharField(max_length=50)),
                ('amt', models.IntegerField(default=0)),
                ('cancel', models.CharField(max_length=50)),
                ('cld', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testpro.cld')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpro.personal')),
                ('tno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpro.train')),
            ],
        ),
        migrations.AddField(
            model_name='cld',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testpro.train'),
        ),
    ]
