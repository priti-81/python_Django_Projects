# Generated by Django 4.2 on 2023-06-26 07:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addpolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 26, 12, 59, 2, 532066))),
                ('policynames', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(blank=True, default='U', max_length=20)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('city', models.CharField(default=None, max_length=20)),
                ('mobile', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='policyTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 26, 12, 59, 2, 535071))),
                ('Name', models.CharField(max_length=30)),
                ('policyTenure', models.SmallIntegerField(default=None)),
                ('totalAmount', models.BigIntegerField(default=None)),
                ('premiumAmount', models.BigIntegerField(default=None)),
                ('premiumPay', models.TextField(default=None)),
                ('expectedReturn', models.BigIntegerField(default=None)),
                ('policyName', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lifesure.addpolicy')),
            ],
        ),
    ]