# Generated by Django 5.0.4 on 2024-06-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.IntegerField(),
        ),
    ]
