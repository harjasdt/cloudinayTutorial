# Generated by Django 4.1.5 on 2023-01-19 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudyapp', '0002_alter_photos_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
