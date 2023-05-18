from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

from .permissions import IsSuperUserOrCritic
from .models import Review
from .serializers import ReviewSerializer
from movies.models import Movie

class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSuperUserOrCritic]

    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"
    
    def get_queryset(self):
        get_object_or_404(Movie, id=self.kwargs.get("movie_id"))

        return Review.objects.filter(movie_id=self.kwargs.get("movie_id"))
    
    def perform_create(self, serializer):
        get_object_or_404(Movie, id=self.kwargs.get("movie_id"))

        return serializer.save(
            movie_id = self.kwargs.get("movie_id"),
            critic = self.request.user
        )

