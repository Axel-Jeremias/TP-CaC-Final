# Generated by Django 4.2.7 on 2023-12-08 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_peliculas', '0004_pelicula_director_alter_pelicula_genero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
