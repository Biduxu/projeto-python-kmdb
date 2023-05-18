from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Review
from users.serializers import UserSerializer
from users.models import User

class UserSerializerReviews(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        read_only_fields = ["id", "first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserSerializerReviews(read_only=True)

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "spoilers", "critic", "movie_id"]
        read_only_fields = ["critic", "movie_id"]
        extra_kwargs = {
            "stars": {
                "validators": [
                    MinValueValidator(
                        limit_value=1
                    ),
                    MaxValueValidator(
                        limit_value=5
                    )
                ]
            }
        }
    
    def create(self, validated_data):
        
        return Review.objects.create(**validated_data)
