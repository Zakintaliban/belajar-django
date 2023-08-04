from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.movielist, name="movies"),
    path("movie/new/", views.new_movie, name="new_movie"),
    path("movie/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("movie/<int:pk>/edit/", views.edit_movie, name="edit_movie"),
    path("movie/<int:pk>/delete/", views.delete_movie, name="delete_movie"),
]
