from django import forms
from .models import MovieList, GenreChoices

class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieList
        fields = ['title', 'genre', 'year']
        widgets = {
            'genre': forms.Select(choices=GenreChoices.choices)
        }
