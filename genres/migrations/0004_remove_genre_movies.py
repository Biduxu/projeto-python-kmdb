# Generated by Django 4.1 on 2023-04-28 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("genres", "0003_genre_movies"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="genre",
            name="movies",
        ),
    ]
