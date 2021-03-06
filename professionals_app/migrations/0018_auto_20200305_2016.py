# Generated by Django 3.0.3 on 2020-03-05 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professionals_app', '0017_user_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.EmailField(max_length=40),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complainant_email', models.EmailField(max_length=40)),
                ('complainant_fname', models.CharField(max_length=10)),
                ('complainant_lname', models.CharField(max_length=10)),
                ('complain_against', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
