# Generated by Django 3.1.4 on 2022-05-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_delete_movielists'),
        ('books', '0004_delete_booklists'),
        ('users', '0007_auto_20220501_1040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookState',
            new_name='BookList',
        ),
        migrations.RenameModel(
            old_name='MovieState',
            new_name='MovieList',
        ),
    ]
