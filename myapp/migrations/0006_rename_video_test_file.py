# Generated by Django 4.1.7 on 2023-04-02 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='video',
            new_name='file',
        ),
    ]
