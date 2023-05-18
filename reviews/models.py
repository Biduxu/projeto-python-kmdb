import uuid

from django.db import models

class Review(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(null=True, default=False)

    critic = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
