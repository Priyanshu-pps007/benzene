# Generated by Django 4.2.3 on 2023-08-05 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_cart_ouruser_mycart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouruser',
            name='mycart',
        ),
    ]