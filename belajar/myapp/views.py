from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import MovieList
from .forms import MovieForm

# Create your views here.


def home(request):
    # return HttpResponse("Hello, Django!")
    return render(request, "home.html", {})


def movielist(request):
    items = MovieList.objects.all()
    return render(request, "movielist.html", {"movies": items})


def movie_detail(request, pk):
    item = get_object_or_404(MovieList, pk=pk)
    return render(request, "movie_detail.html", {"movie": item})


def new_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect("movie_detail", pk=movie.pk)
    else:
        form = MovieForm()
    return render(
        request,
        "movie_form.html",
        {"form": form, "title": "New Movie", "cancel_url": reverse("movies")},
    )


def edit_movie(request, pk):
    movie = get_object_or_404(MovieList, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect("movie_detail", pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(
        request,
        "movie_edit.html",
        {
            "form": form,
            "title": "Edit Movie",
            "movie": movie,  # tambahkan ini ke konteks
            "cancel_url": reverse("movie_detail", args=[pk]),
        },
    )


def delete_movie(request, pk):
    movie = get_object_or_404(MovieList, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movies")
    return render(request, "movie_confirm_delete.html", {"movie": movie})
