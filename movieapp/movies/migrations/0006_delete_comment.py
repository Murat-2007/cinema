# Generated by Django 3.2.3 on 2022-06-13 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
