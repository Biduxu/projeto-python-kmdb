from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsSuperuser


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
