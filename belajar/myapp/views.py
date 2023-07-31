from django.shortcuts import render, HttpResponse
from .models import MovieList

# Create your views here.


def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, "home.html", {})


def movielist(request):
    items = MovieList.objects.all()
    return render(request, "movielist.html", {"movies": items})
