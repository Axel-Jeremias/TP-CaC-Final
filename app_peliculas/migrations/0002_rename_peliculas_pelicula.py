# Generated by Django 4.2.7 on 2023-12-02 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_peliculas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Peliculas',
            new_name='Pelicula',
        ),
    ]