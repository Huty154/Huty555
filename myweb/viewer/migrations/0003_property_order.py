# Generated by Django 4.2.6 on 2023-11-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
