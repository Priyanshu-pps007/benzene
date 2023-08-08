# Generated by Django 4.2.3 on 2023-08-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_order_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleven', models.ManyToManyField(null=True, to='myapp.eleventh')),
                ('twelve', models.ManyToManyField(null=True, to='myapp.twelveth')),
            ],
        ),
        migrations.AddField(
            model_name='ouruser',
            name='mycart',
            field=models.ManyToManyField(null=True, to='myapp.cart'),
        ),
    ]