# Generated by Django 4.1 on 2023-04-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_remove_movie_genres"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="genres",
            field=models.ManyToManyField(related_name="movies", to="movies.movie"),
        ),
    ]
