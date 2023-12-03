# Generated by Django 4.2.7 on 2023-12-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postal', models.BigIntegerField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]