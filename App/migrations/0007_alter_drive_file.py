# Generated by Django 4.0.3 on 2022-03-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_rename_test_drive_rename_folder_drive_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='File',
            field=models.FileField(upload_to='userfiles/%y/%m/%d'),
        ),
    ]
