# Generated by Django 4.1 on 2023-04-27 14:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                (
                    "movies",
                    models.ManyToManyField(related_name="genres", to="movies.movie"),
                ),
            ],
        ),
    ]
