from rest_framework import serializers

from .models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.ListField(write_only=True)
    
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "duration", "premiere", "budget", "overview", "genres"]
        read_only_fields = ["id", "genres"]
        depth = 0

    def create(self, validated_data):

        genres_data = validated_data["genres"]
        list_genres = []
        
        for genre in genres_data:
            found_genre = Genre.objects.filter(name=genre["name"]).first()

            if(found_genre):
                list_genres.append(found_genre)
            else:
                new_genre = Genre.objects.create(
                    name = genre["name"]
                )

                list_genres.append(new_genre)
        
        has_overview = False

        for key in validated_data:
            if(key == "overview"):
                has_overview = True

        if(has_overview):
            movie = Movie.objects.create(
                title = validated_data["title"],
                duration = validated_data["duration"],
                premiere = validated_data["premiere"],
                budget = validated_data["budget"],
                overview = validated_data["overview"],
                user = validated_data["user"]
            )
        else:
            movie = Movie.objects.create(
                title = validated_data["title"],
                duration = validated_data["duration"],
                premiere = validated_data["premiere"],
                budget = validated_data["budget"],
                user = validated_data["user"]
            )
        
        for genre in list_genres:
            genre.movies.add(movie)

        return movie
