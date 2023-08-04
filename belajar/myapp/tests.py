from django.test import TestCase
from .models import MovieList, GenreChoices

# Create your tests here.


class MovieListTestCase(TestCase):
    def setUp(self):
        MovieList.objects.create(
            title="Test Movie", genre=GenreChoices.ACTION, year=2022
        )

    def test_movie_list_created(self):
        """MovieList objects are saved properly"""
        movie = MovieList.objects.get(title="Test Movie")
        self.assertEqual(movie.genre, GenreChoices.ACTION)
        self.assertEqual(movie.year, 2022)
