# Generated by Django 4.2 on 2023-06-26 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lifesure', '0002_alter_addpolicy_created_alter_policytable_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpolicy',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 26, 17, 31, 54, 781809)),
        ),
        migrations.AlterField(
            model_name='policytable',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 26, 17, 31, 54, 784808)),
        ),
        migrations.AlterField(
            model_name='policytable',
            name='totalAmount',
            field=models.IntegerField(default=123456),
        ),
    ]