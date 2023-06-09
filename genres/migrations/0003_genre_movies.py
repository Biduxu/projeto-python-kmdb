# Generated by Django 4.1 on 2023-04-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_remove_movie_genres"),
        ("genres", "0002_remove_genre_movies"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="movies",
            field=models.ManyToManyField(related_name="genres", to="movies.movie"),
        ),
    ]
