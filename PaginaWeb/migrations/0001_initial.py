# Generated by Django 5.1 on 2024-10-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('fono', models.CharField(max_length=15)),
                ('tipo', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=25)),
            ],
        ),
    ]