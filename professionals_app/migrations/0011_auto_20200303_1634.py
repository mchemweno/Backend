# Generated by Django 3.0.3 on 2020-03-03 13:34

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('professionals_app', '0010_auto_20200303_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_pictures/%y/%m/%d'),
        ),
    ]
