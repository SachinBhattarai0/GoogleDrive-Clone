# Generated by Django 4.0.3 on 2022-03-25 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_test_folder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='test',
            new_name='Drive',
        ),
        migrations.RenameField(
            model_name='drive',
            old_name='folder',
            new_name='File',
        ),
    ]