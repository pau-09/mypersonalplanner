# Generated by Django 3.1.4 on 2022-05-02 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_delete_movielists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='genero',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='titulo',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='anio',
            new_name='year',
        ),
    ]