# Generated by Django 5.1 on 2024-11-14 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default=1, max_length=13),
        ),
    ]