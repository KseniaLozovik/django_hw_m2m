# Generated by Django 3.1.2 on 2023-04-18 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20230418_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='is_main',
        ),
    ]
