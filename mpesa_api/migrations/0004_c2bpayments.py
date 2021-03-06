# Generated by Django 3.0.3 on 2020-03-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa_api', '0003_auto_20200305_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='C2BPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionType', models.CharField(blank=True, max_length=20)),
                ('TransID', models.CharField(blank=True, max_length=15)),
                ('TransTime', models.CharField(blank=True, max_length=14)),
                ('TransAmount', models.CharField(blank=True, max_length=10)),
                ('BusinessShortCode', models.CharField(blank=True, max_length=8)),
                ('BillRefNumber', models.CharField(blank=True, max_length=20)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=20)),
                ('OrgAccountBalance', models.CharField(blank=True, max_length=12)),
                ('ThirdPartyTransID', models.CharField(blank=True, max_length=20)),
                ('MSISDN', models.CharField(blank=True, max_length=12)),
                ('FirstName', models.CharField(blank=True, max_length=20)),
                ('MiddleName', models.CharField(blank=True, max_length=20)),
                ('LastName', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
