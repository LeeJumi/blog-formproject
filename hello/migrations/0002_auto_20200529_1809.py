# Generated by Django 3.0.6 on 2020-05-29 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='boby',
            new_name='body',
        ),
    ]