# Generated by Django 4.1.5 on 2023-01-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudyapp', '0004_photos_cc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='id',
        ),
        migrations.AlterField(
            model_name='photos',
            name='title',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
