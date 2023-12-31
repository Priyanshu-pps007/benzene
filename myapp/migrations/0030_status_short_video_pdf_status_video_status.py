# Generated by Django 4.2.3 on 2023-08-07 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_ouruser_razorpay_order_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Demo', models.CharField(blank=True, default='Demo', max_length=10, null=True)),
                ('Paid', models.CharField(blank=True, default='Paid', max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='short_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(default='', max_length=500, null=True)),
                ('chapter_name', models.CharField(default='', max_length=500)),
                ('video', models.FileField(upload_to='Media')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.status')),
            ],
        ),
        migrations.AddField(
            model_name='pdf',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.status'),
        ),
        migrations.AddField(
            model_name='video',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.status'),
        ),
    ]
