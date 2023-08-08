# Generated by Django 4.1.7 on 2023-07-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_chemistry_chapter_name_pdf_chapter_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='eleventh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sno', models.CharField(max_length=50)),
                ('chapter_name', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(default='', max_length=500, unique=True)),
                ('video', models.FileField(upload_to='Media')),
            ],
        ),
        migrations.DeleteModel(
            name='chemistry',
        ),
        migrations.AlterField(
            model_name='pdf',
            name='chapter_name',
            field=models.CharField(default='', max_length=500, unique=True),
        ),
        migrations.AddField(
            model_name='eleventh',
            name='pdfs',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.pdf'),
        ),
        migrations.AddField(
            model_name='eleventh',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, to='myapp.video'),
        ),
    ]
