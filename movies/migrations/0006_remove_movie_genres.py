# Generated by Django 4.1 on 2023-04-28 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0005_alter_movie_genres"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="genres",
        ),
    ]