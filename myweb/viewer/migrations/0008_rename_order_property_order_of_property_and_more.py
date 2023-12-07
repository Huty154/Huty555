# Generated by Django 4.2.7 on 2023-12-07 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_property_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='order',
            new_name='order_of_property',
        ),
        migrations.AddField(
            model_name='order',
            name='property_object',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='viewer.property'),
            preserve_default=False,
        ),
    ]
