# Generated by Django 3.0.3 on 2020-03-04 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professionals_app', '0014_auto_20200304_0401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='service',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
