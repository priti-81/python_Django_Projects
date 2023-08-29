# Generated by Django 4.2 on 2023-08-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeonline', '0007_alter_userselectamenities_saler_infoid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salerinfo',
            name='video_file',
            field=models.FileField(blank=True, default=None, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='salerinfo',
            name='Area',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='salerinfo',
            name='BHK',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='UserUploadVideos',
        ),
    ]
