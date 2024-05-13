from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Film


class FilmListView(ListView):
    model = Film
    template_name = 'all_films_view.html'


class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail_view.html'


class FilmCreateView(CreateView):
    model = Film
    template_name = 'create_film.html'
    fields = '__all__'
    success_url = '/films'


class FilmUpdateView(UpdateView):
    model = Film
    template_name = 'update_film.html'
    fields = '__all__'
    success_url = '/films'


class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'delete_film.html'
    success_url = '/films'


def get_film_actors(request, pk):
    film = Film.objects.get(pk=pk)
    actors = film.actors.all()
    data = {'actors': actors}
    return render(request, template_name='film_actors_view.html', context=data)
