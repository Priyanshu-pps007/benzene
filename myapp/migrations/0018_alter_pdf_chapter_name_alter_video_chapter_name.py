# Generated by Django 4.1.7 on 2023-07-30 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_pdf_pdf_title_video_video_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='chapter_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='chapter_name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
