# Generated by Django 3.2.3 on 2022-06-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20220426_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_cover',
            field=models.ImageField(upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_name',
            field=models.ImageField(upload_to='movies'),
        ),
    ]
