# Generated by Django 4.1.1 on 2022-11-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='mobilenumber',
            field=models.CharField(max_length=12),
        ),
    ]