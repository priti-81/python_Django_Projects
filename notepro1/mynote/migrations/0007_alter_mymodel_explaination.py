# Generated by Django 4.2 on 2023-06-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynote', '0006_alter_mymodel_explaination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='Explaination',
            field=models.TextField(blank=True, null=True),
        ),
    ]
