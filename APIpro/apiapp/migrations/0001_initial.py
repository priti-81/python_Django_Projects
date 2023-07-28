# Generated by Django 4.2 on 2023-07-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=30)),
                ('Isbn', models.IntegerField()),
                ('Publisher', models.CharField(max_length=40)),
            ],
        ),
    ]
