# Generated by Django 3.0.3 on 2020-03-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0002_auto_20200305_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='checkout_request_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='merchant_request_id',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='mpesa_receipt_number',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='mpesa_transaction_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='result_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lipanampesaonline',
            name='result_description',
            field=models.CharField(max_length=120),
        ),
    ]
