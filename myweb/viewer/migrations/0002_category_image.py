# Generated by Django 4.2.6 on 2023-11-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
