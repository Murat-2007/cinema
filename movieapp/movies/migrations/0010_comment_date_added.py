# Generated by Django 3.2.3 on 2022-09-16 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_comment_e_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]