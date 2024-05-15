from django.shortcuts import render, redirect, get_object_or_404
from .models import Actor
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import ActorForm


def all_actors_list(request):
    all_actors = Actor.objects.all()
    data = {'actors': all_actors}
    return render(request, template_name='actors_list_view.html', context=data)


def actor_view(request, pk):
    actor = Actor.objects.get(pk=pk)
    data = {'actor': actor}
    return render(request, template_name='actor_detail_view.html', context=data)


def create_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/actors')
    else:
        form = ActorForm()
    return render(request, 'create_actor.html', {'form': form})


def update_actor(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('/actors')
    else:
        form = ActorForm(instance=actor)
    return render(request, 'update_actor.html', {'form': form})


class ActorListView(ListView):
    model = Actor
    template_name = 'actors_list_view.html'


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'actor_detail_view.html'


class ActorCreateView(CreateView):
    model = Actor
    template_name = 'create_actor.html'
    fields = '__all__'
    success_url = '/actors'


class ActorUpdateView(UpdateView):
    model = Actor
    template_name = 'update_actor.html'
    fields = '__all__'
    success_url = '/actors'


class ActorDeleteView(DeleteView):
    model = Actor
    template_name = 'delete_actor.html'
    success_url = '/actors'
