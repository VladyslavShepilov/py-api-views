from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    movie_list,
    movie_detail,
    GenreListView,
    GenreDetailView,
    ActorListView,
    ActorDetailView,
    CinemaHallListVew,
    CinemaHallDetailView,
    MovieViewSet
)

routers = routers.DefaultRouter()
routers.register("movies", MovieViewSet)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallListVew.as_view(), name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallDetailView.as_view(), name="cinema-hall-detail"),
    path("movies/", include(routers.urls))
]

app_name = "cinema"
