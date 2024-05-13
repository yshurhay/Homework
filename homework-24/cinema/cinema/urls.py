"""
URL configuration for cinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from actors.views import create_actor, all_actors_list, actor_view, update_actor
from movie.views import FilmListView, FilmDetailView, FilmCreateView, FilmUpdateView, FilmDeleteView, get_film_actors


urlpatterns = [
    path('admin/', admin.site.urls),
    path('actors/', all_actors_list),
    path('actors/<int:pk>', actor_view),
    path('create_actor', create_actor),
    path('update_actor/<int:pk>', update_actor),
    path('films/', FilmListView.as_view()),
    path('films/<int:pk>', FilmDetailView.as_view()),
    path('create_film/', FilmCreateView.as_view()),
    path('update_film/<int:pk>', FilmUpdateView.as_view()),
    path('delete_film/<int:pk>', FilmDeleteView.as_view()),
    path('films/<int:pk>/actors', get_film_actors),
]
