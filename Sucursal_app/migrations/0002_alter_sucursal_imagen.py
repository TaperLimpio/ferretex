# Generated by Django 5.1 on 2024-11-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sucursal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='imagen',
            field=models.ImageField(upload_to='sucursal-imagenes/'),
        ),
    ]