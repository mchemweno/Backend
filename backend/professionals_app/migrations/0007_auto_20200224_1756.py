# Generated by Django 3.0.3 on 2020-02-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals_app', '0006_review_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.EmailField(max_length=25),
        ),
    ]
