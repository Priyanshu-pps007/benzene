# Generated by Django 4.2.3 on 2023-08-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_remove_eleventh_status_twelveth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouruser',
            name='chem1',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='chem2',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='maths1',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='maths2',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='physics1',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='physics2',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='ouruser',
            name='subject6',
        ),
        migrations.AddField(
            model_name='ouruser',
            name='eleven',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.eleventh'),
        ),
        migrations.AddField(
            model_name='ouruser',
            name='twelve',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.twelveth'),
        ),
    ]
