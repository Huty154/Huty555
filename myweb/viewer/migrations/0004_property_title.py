# Generated by Django 4.2.6 on 2023-11-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_property_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='title',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
